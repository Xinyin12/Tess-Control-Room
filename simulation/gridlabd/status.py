"""Display market status"""

import sys, os
import sqlite3
import datetime as dt
import time
from database import Tess2Database
import database
database.QUIET = True

if len(sys.argv) == 1:
    DATABASE_NAME = "gridlabd.db"
else:
    DATABASE_NAME = sys.argv[1]

# 
# Display most recent auction
#
labels = dict(
    market_time = "Cleared    ",
    resource_id = "Resource              ",
    quantity = " Quantity",
    units = "Units ",
    price = "  Price",
    next_clearing = "Next clear ",
    orders = " Orders",
    hc = " HC",
    hw = " HW",
    pv = " PV",
    ev = " EV",
    es = " ES",
    )

def home():
    print("\033[H")

def writeln(*args,**kwargs):
    print("\033[K"+' '.join([str(x) for x in args]),**kwargs)

def clear():
    print("\033[H\033[2J")

def hide_cursor():
    print("\033[?25h")

def show_cursor():
    print("\033[25l")

clear()
while True:
    try:
        db = Tess2Database(DATABASE_NAME)

        def get_setting(group,name):
            cursor = db.select_settings_value(group,name)
            return cursor.fetchone()[0]

        #
        # Read market data
        #
        cursor0 = db.select_markets_resourceid_units_interval()
        markets = {}
        intervals = {}
        for row in cursor0.fetchall():
            resource_id = row[0]
            units = row[1]
            interval = row[2]
            if resource_id not in markets.keys():
                markets[resource_id] = {}
            markets[resource_id][interval] = units
            if interval not in intervals.keys():
                intervals[interval] = []
            intervals[interval].append(resource_id)

        home()
        hide_cursor()
        writeln("TESS Status at %s (for developer use only)" % dt.datetime.now().strftime("%m/%d/%y %H:%M:%S"))
        writeln("")
        writeln("Utility: ",get_setting('utility','name'))
        writeln("Database: ",DATABASE_NAME)
        writeln("")
        widths = []
        for name in labels.values():
            widths.append(-len(name) if name.endswith(' ') else len(name))
            writeln(f"%{widths[-1]}s"%name,end="   ")
        writeln("")
        for col, name in enumerate(labels.values()):
            writeln("-"*abs(widths[col]),end="   ")
        writeln("")

        for interval in intervals.keys():
            market_id = int(dt.datetime.now().timestamp()/interval)
            cursor1 = db.select_auctions_markettime_resourceid_quantity_price_auctionid(market_id)
            names = [x[0] for x in cursor1.description]
            timestamp = dt.datetime.fromtimestamp(market_id*interval)
            counts = {}
            for device_type in ["HC","HW","PV","EV","ES"]:
                cursor2 = db.select_orders_countorderid_resourceid(market_id+1,device_type)
                for item in cursor2.fetchall():
                    count = int(item[0])
                    resource_id = item[1]
                    if not resource_id in counts.keys():
                        counts[resource_id] = dict(total=0,HC=0,HW=0,PV=0,EV=0,ES=0)
                    counts[resource_id][device_type] += count
                    counts[resource_id]['total'] += count
            for item in cursor1.fetchall():
                try:
                    values = dict(zip(names,item))
                    market_time = dt.datetime.fromtimestamp(values['market_time']).strftime('%m/%d %H:%M')
                    resource_id = values['resource_id']
                    quantity = values['quantity']
                    price = values['price']
                    next_clearing = dt.datetime.fromtimestamp(values['market_time']+interval).strftime('%m/%d %H:%M')
                    writeln(f"%{widths[0]}s   %{widths[1]}s   %{widths[2]}.1f   %{widths[3]}s   %{widths[4]}.2f   %{widths[5]}s   %{widths[6]}d   %{widths[7]}d   %{widths[8]}d   %{widths[8]}d   %{widths[9]}d   %{widths[10]}d" 
                        % (market_time,resource_id,quantity,markets[resource_id][interval],price,next_clearing,*counts[resource_id].values()))
                except:
                    e_type, e_value, e_trace = sys.exc_info()
                    writeln("ERROR:",e_type.__name__,e_value,file=sys.stderr)
            db.rollback()

        writeln("")

        writeln(f"Table          Count")
        writeln(f"------------ -------")
        for table, label in dict(
            settings = "Settings",
            markets = "Markets",
            auctions = "Auctions",
            agents = "Agents",
            devices = "Devices",
            meters = "Meters",
            orders = "Orders",
            dispatches = "Dispatches",
            settlements = "Settlements",
            weather = "Weather",
            ).items():
            try:
                cursor3 = db.select_count(table)
                writeln(f"{label:12s} {cursor3.fetchone()[0]:7d}")
            except:
                writeln(f"{label:12s}       -")

        writeln("")

        writeln("Cash flow")
        writeln("========================")
        value = db.select_settlements_sum(subtotal='revenue').fetchone()[0]
        writeln(f"  Receipts: {(value if value else 0.0):10.2f}")
        value = db.select_settlements_sum(subtotal='expense').fetchone()[0]
        writeln(f"  Payments: {(value if value else 0.0):10.2f}")
        writeln(f"            ----------")
        value = db.select_settlements_sum().fetchone()[0]
        writeln(f"  Revenues: {(value if value else 0.0):10.2f}")
        writeln("========================")

        writeln("")

        writeln(f"Log size: {os.path.getsize(os.path.splitext(DATABASE_NAME)[0]+'.log')/1e6:.1f} MB")

        writeln("")

        writeln("Ctrl-C to stop")
        show_cursor()

    except:
        e_type, e_value, e_trace = sys.exc_info()
        e_file = os.path.basename(os.path.split(e_trace.tb_frame.f_code.co_filename)[1])
        e_line = e_trace.tb_lineno
        writeln(f"ERROR [{e_file}@{e_line}]: {e_type.__name__} {e_value}",file=sys.stderr)

    time.sleep(1)
