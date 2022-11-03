"""Simulation DB API

The Tess2Database class emulates the database API for TESS2. The general
naming convention for methods is <action>_<table>_<fields>(<args...>). Most
methods return the result of the `execute()` call or raise the appropriate
exception if necessary. In the case of `select` methods, the return value is
usually the cursor.

In addition, the `commit()` and `rollback()` methods are made available
directly to instances of the class.
"""

import os, sys
import sqlite3
import datetime as dt
import re

twospaces = re.compile("\\s\\s+")

QUIET = False

def now():
    return dt.datetime.now().timestamp()

def error(msg):
    if not QUIET:
        print(f"ERROR [database]: {msg}",file=sys.stderr)

class Tess2Database:

    max_logtime = dt.timedelta(minutes=1)

    def __init__(self,db,autolog=True):
        self.db = sqlite3.connect(db)
        if autolog:
            self.logfile = os.path.splitext(db)[0] + ".log"
            self.backupfile = os.path.splitext(db)[0] + ".bak"
            self.log = open(self.logfile,"w")
            self.logtime = dt.datetime.now() + self.max_logtime

    def set_now(self,call):
        global now
        now = call

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def run_script(self,sqlfile):
        with open(sqlfile,"r") as fh:
            for query in ''.join(fh.readlines()).split(';'):
                try:
                    self.put(query)
                except:
                    e_type, e_value, e_trace = sys.exc_info()
                    error(f"{query}: {e_type.__name__} {e_value}")
                    raise

    def get(self,command,ignore=[]):
        try:
            return self.db.execute(command)
        except:
            e_type, e_value, e_trace = sys.exc_info()
            if not e_type in ignore:
                error(f"SQL query [{command}] failed: {e_type.__name__} {e_value}")
            raise

    def put(self,command,ignore=[]):
        try:
            return self.db.execute(command)
        except:
            e_type, e_value, e_trace = sys.exc_info()
            if not e_type in ignore:
                error(f"SQL query [{command}] failed: {e_type.__name__} {e_value}")
            raise
        finally:
            self.add_log(command)

    def restore(self):
        self.commit()
        with sqlite3.connect(self.backupfile) as db:
            db.backup(self.db)

    def backup(self):
        self.commit()
        with sqlite3.connect(self.backupfile) as db:
            self.db.commit()
            self.db.backup(db)

    def add_log(self,command):
        # if self.logtime < dt.datetime.now():
        #     self.backup()
        #     self.log = open(self.logfile,"w")
        #     self.logtime = dt.datetime.now() + self.max_logtime
        # print(twospaces.sub(" ",command).strip(),file=self.log)
        return

    def dump(self,prefix=""):
        self.commit()
        cur = self.get("select name from sqlite_master where type = 'table'")
        tables = [x[0] for x in cur.fetchall()]
        self.db.rollback()
        for table in tables:
            cur = self.db.execute(f"select * from {table}")
            header = [x[0] for x in cur.description]
            data = cur.fetchall()
            self.db.rollback()
            with open(f"{prefix}{table}.csv","w") as csv:
                print(','.join(header),file=csv)
                for row in data:
                    values = [str(x) for x in row]
                    print(','.join([f'"{x}"' if ',' in x else x for x in values]),file=csv)
                csv.close()

    def replace_settlements(self,record_time,order_id,cost,valid_at=None):
        return self.put(f"""
            replace into settlements 
            (record_time, order_id, cost, valid_at) 
            values 
            ('{record_time}','{order_id}',{cost},'{valid_at if valid_at else now()}');
            """)

    def insert_settings(self,setting_id,device_id,name,value,valid_at=None):
        return self.put(f"""
            insert into settings
            (setting_id,device_id,name,valid_at,value)
            values
            ('{setting_id}','{device_id}','{name}','{valid_at if valid_at else now()}','{value}');
            """)

    def insert_agents(self,agent_id,resource_id,valid_at=None):
        return self.put(f"""
            insert into agents 
            (agent_id,resource_id,valid_at) 
            values 
            ('{agent_id}','{resource_id}','{valid_at if valid_at else now()}');
            """)

    def insert_markets(self,resource_id,units,interval,valid_at=None):
        return self.put(f"""
            insert into markets
            ( resource_id, units, interval, valid_at)
            values
            ('{resource_id}','{units}',{interval},'{valid_at if valid_at else now()}');
            """)

    def insert_auctions(self,auction_id,market_id,market_time,resource_id,price,quantity,marginal_type,marginal_order,marginal_quantity,marginal_rank,valid_at=None):
        return self.put(f"""
            insert into auctions (auction_id,market_id,market_time,resource_id,price,quantity,marginal_type,marginal_order,marginal_quantity,marginal_rank,valid_at)
            values ('{auction_id}','{market_id}','{market_time}','{resource_id}',{price},{quantity},'{marginal_type}','{marginal_order}',{marginal_quantity},{marginal_rank},'{valid_at if valid_at else now()}');
            """)

    def insert_devices(self,device_id,agent_id,device_type,valid_at=None):
        return self.put(f"""
            insert into devices
            (device_id, agent_id, device_type, valid_at)
            values
            ('{device_id}','{agent_id}','{device_type}','{valid_at if valid_at else now()}');
            """)

    def insert_dispatches(self,record_time, order_id, quantity,valid_at=None):
        return self.put(f"""
            insert into dispatches 
            (record_time, order_id, quantity, valid_at) 
            values 
            ('{record_time}','{order_id}',{quantity},'{valid_at if valid_at else now()}');
            """,ignore=[sqlite3.IntegrityError])

    def replace_orders(self,record_time,order_id,device_id,resource_id,market_id,quantity,price,flexible,state,valid_at=None):
        return self.put(f"""
            replace into orders
            (record_time,order_id,device_id,resource_id,market_id,quantity,price,flexible,state,valid_at)
            values
            ('{record_time}','{order_id}','{device_id}','{resource_id}','{market_id}',{quantity},{price},{flexible},{state},'{valid_at if valid_at else now()}');
            """)

    def select_settings_value(self,device_id,name):
        return self.get(f"""
            select value 
            from settings
            where device_id = '{device_id}' and name = '{name}'
            order by valid_at desc;
            """)

    def select_markets_resourceid_units_interval(self):
        return self.get(f"""
            select resource_id, units, interval 
            from markets;
            """)
    
    def select_auctions_markettime_resourceid_quantity_price_auctionid(self,market_id):
        return self.get(f"""
            select market_time, resource_id, quantity, price, auction_id 
            from auctions 
            where market_id = {market_id} 
            order by resource_id;
            """)

    def select_orders_countorderid_resourceid(self,market_id,device_type):
        return self.get(f"""
            select count(order_id), resource_id 
            from orders 
            join devices on orders.device_id = devices.device_id 
            where market_id = {market_id} and device_type = '{device_type}'
            group by resource_id;
            """)

    def select_count(self,table):
        return self.get(f"""select count(*) 
            from {table};
            """)

    def select_settlements_sum(self,subtotal=None):
        if subtotal == 'revenue':
            where = "where cost > 0"
        elif subtotal == 'expense':
            where = "where cost < 0"
        elif subtotal is None:
            where = ""
        else:
            raise Tess2DatabaseException("subtotal must on of [None,'revenue','expense']")
        return self.get(f"""
            select sum(cost) 
            from settlements
            {where};
            """)

    def insert_weather(self,location,temperature,humidity,solar,wind_speed,wind_direction,valid_at=None):
        return self.put(f"""
            insert into weather 
            (location,temperature,humidity,solar,wind_speed,wind_direction,valid_at)
            values 
            ('{location}',{temperature},{humidity},{solar},{wind_speed},{wind_direction},'{valid_at if valid_at else now()}');
            """)

    def insert_meter(self,meter_id,device_id,real_power,reactive_power=None,valid_at=None):
        return self.put(f"""
            insert into meters 
            (meter_id,device_id,real_power,reactive_power,valid_at)
            values 
            ('{meter_id}','{device_id}',{real_power},{reactive_power if reactive_power else 'NULL'},'{valid_at if valid_at else now()}');
            """)
