"""Display market status"""

import sys, os
import sqlite3
import datetime as dt
import time
from database import Tess2Database

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

        print("\033[H\033[2JTESS Status at %s (for developer use only)" % dt.datetime.now().strftime("%m/%d/%y %H:%M:%S"))
        print("")
        print("Utility: ",get_setting('global','utility_name'))
        print("Database: ",DATABASE_NAME)
        print("")
        widths = []
        for name in labels.values():
            widths.append(-len(name) if name.endswith(' ') else len(name))
            print(f"%{widths[-1]}s"%name,end="   ")
        print("")
        for col, name in enumerate(labels.values()):
            print("-"*abs(widths[col]),end="   ")
        print("")

        for interval in intervals.keys():

            market_id = int(dt.datetime.now().timestamp()/interval)
            cursor1 = db.select_auctions_markettime_resourceid_quantity_price_auctionid(market_id)
            print("select_auctions_markettime_resourceid_quantity_price_auctionid with marketId:",market_id,cursor1.fetchall())
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
                    print(f"%{widths[0]}s   %{widths[1]}s   %{widths[2]}.1f   %{widths[3]}s   %{widths[4]}.2f   %{widths[5]}s   %{widths[6]}d   %{widths[7]}d   %{widths[8]}d   %{widths[8]}d   %{widths[9]}d   %{widths[10]}d" 
                        % (market_time,resource_id,quantity,markets[resource_id][interval],price,next_clearing,*counts[resource_id].values()))
                except:
                    e_type, e_value, e_trace = sys.exc_info()
                    print("ERROR:",e_type.__name__,e_value,file=sys.stderr)
            db.rollback()

        print("")

        print(f"Table          Count")
        print(f"------------ -------")
        for table, label in dict(
            settings = "Settings",
            markets = "Markets",
            auctions = "Auctions",
            agents = "Agents",
            devices = "Devices",
            orders = "Orders",
            dispatches = "Dispatches",
            settlements = "Settlements",
            ).items():
            cursor3 = db.select_count(table)
            print(f"{label:12s} {cursor3.fetchone()[0]:7d}")

        print("")

        cursor = db.select_settlements_sum()
        print(f"Settled costs: {cursor.fetchone()[0]:.2f}")

        print("")

        print(f"Log size: {os.path.getsize(os.path.splitext(DATABASE_NAME)[0]+'.log')/1e6:.1f} MB")

        print("")

        print("Ctrl-C to stop")

    except:
        e_type, e_value, e_trace = sys.exc_info()
        print("ERROR:",e_type.__name__,e_value,file=sys.stderr)

    time.sleep(1)
