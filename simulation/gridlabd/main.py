"""Realtime simulation main python module

To use this module in a GridLAB-D model, include the following GLM directive

   #include "main.glm"
"""
import sys, os
import datetime as dt
import random
import uuid
import time
import sqlite3
from database import Tess2Database
import devices

# 
# Options
#

OPTIONS = {
    "verbose" : False,
    "warning" : False,
    "debug" : False,
    "progress" : False,
    "newdb" : False,
    }

def verbose(msg):
    if OPTIONS['verbose']:
        print(f"VERBOSE [{__name__}.py]: {msg}", file=sys.stderr)

def error(msg):
    gridlabd.error(msg)

def debug(msg):
    if OPTIONS['debug']:
        frame = sys._getframe(1)
        file = os.path.basename(frame.f_code.co_filename)
        name = frame.f_code.co_name
        line = frame.f_lineno
        print(f"DEBUG [{file}/{name}@{line}]: {msg}", file=sys.stderr)

def warning(msg):
    if not OPTIONS['warning']:
        gridlabd.warning(msg)

def progress(msg):
    if OPTIONS['progress']:
        print(msg,file=sys.stderr)
#
# Database
#

DATABASE = None

#
# Utilities
#

def guid():
    """Return a globally unique id"""
    return uuid.uuid4().hex[2:]

def timestep(t0,ts,timeout=3600):
    """Advanced to the next timestep after wait"""
    debug(f"timestep(t0={dt.datetime.fromtimestamp(t0)},ts={ts}s,timeout={timeout}s)")
    now = dt.datetime.now().timestamp()
    wait = round(t0 - now,6)
    debug(f"  now = {dt.datetime.fromtimestamp(now)}, wait = {wait} seconds")
    if wait > 0:
        pause = min(wait,timeout) if timeout else wait
        debug(f"  waiting {pause} seconds from {dt.datetime.fromtimestamp(now)}")
        time.sleep(pause)
        t1 = int(now)+min(ts,timeout)
    elif -wait < ts:
        t1 = int(now)+1
    else:
        t1 = int(t0/ts+1)*ts
    debug(f"  --> {dt.datetime.fromtimestamp(t1)} ")
    return t1

#
# Initialization
#

SIMNOW = 0
def now():
    global SIMNOW
    return SIMNOW

def init_options(varname):
    PYTHON_OPTIONS = gridlabd.get_global(varname).strip('"').split(",")
    if '' in PYTHON_OPTIONS:
        PYTHON_OPTIONS.remove('')
    global OPTIONS
    for key in OPTIONS.keys():
        if key in PYTHON_OPTIONS:
            OPTIONS[key] = True
            PYTHON_OPTIONS.remove(key)
    if len(PYTHON_OPTIONS) > 0:
        error(f"{os.path.basename(gridlabd.get_global('modelname'))} global {varname} '{','.join(PYTHON_OPTIONS)}' invalid")

def on_init(t):
    init_options("PYTHON_OPTIONS")
    debug(f"connecting to sqlite database")
    dbname = gridlabd.get_global('DATABASE')
    if OPTIONS['newdb'] and os.path.exists(dbname) and not gridlabd.get_global("TEST"):
        debug(f"PYTHON_OPTIONS=newdb is destroying '{dbname}'")
        os.remove(dbname)
    global DATABASE
    if gridlabd.get_global("TEST"):
        DATABASE = Tess2Database(":memory:")
    else:
        DATABASE = Tess2Database(dbname)
    global SIMNOW
    SIMNOW = t
    DATABASE.set_now(now)
    devices.init(gridlabd=gridlabd,DATABASE=DATABASE)
    DATABASE.run_script(gridlabd.get_global('SQLITE_SCHEMA'))
    verbose(f"starting wayback from {dt.datetime.fromtimestamp(t)}...")
    return True

def utility_init(obj,t):
    print('Setting utility name to',obj)
    DATABASE.insert_settings(guid(),'utility','name',obj)
    return 0

#
# Termination
#

def on_term(t):
    DATABASE.dump("dump_")

#
# Precommit/Commit
#

def on_precommit(t):
    global SIMNOW
    SIMNOW = t
    debug(f"t={SIMNOW}")
    try:
        DATABASE.commit()
    except:
        warning(f"database commit failed at {dt.datetime.fromtimestamp(t)}")
    return devices.update(t)

def on_commit(t):
    debug(f"t={dt.datetime.fromtimestamp(t)}")
    try:
        DATABASE.commit()
        progress(f"database commit at {dt.datetime.fromtimestamp(t)}, press Ctrl-C to stop")
    except:
        warning(f"database commit failed at {dt.datetime.fromtimestamp(t)}")
    return gridlabd.NEVER

#
# Weather
#
def weather_commit(obj,t):
    if t % 60 == 0:
        data = gridlabd.get_object(obj)
        DATABASE.insert_weather(data["city"],float(data["temperature"].split()[0]),float(data["humidity"].split()[0])*100,float(data["solar_global"].split()[0]),float(data["wind_speed"].split()[0])*2.24,float(data["wind_dir"].split()[0]))
    return gridlabd.NEVER

#
# Agents
#

def agent_init(obj,t):
    resource_id = gridlabd.get_value(obj,"resource_id")
    DATABASE.insert_agents(obj,resource_id)
    return 0

#
# Auctions
#

def auction_init(obj,t):
    resource_id = gridlabd.get_value(obj,'resource_id')
    units = gridlabd.get_value(obj,'units')
    interval = gridlabd.get_value(obj,'interval')
    DATABASE.insert_markets(resource_id,units,interval)
    return 0

def auction_precommit(obj,t):
    debug(f"obj={obj}, t={dt.datetime.fromtimestamp(t)}")
    auction = gridlabd.get_object(obj)
    interval = int(auction["interval"])
    if t % interval == 0:

        # generate a random clearing (TODO: use the actual clearing code)
        AUCTIONID = int(t/interval)
        MARKETTIME = t
        price_mean = float(gridlabd.get_value(obj,'price_mean'))
        price_std = float(gridlabd.get_value(obj,'price_std'))
        price_floor = float(gridlabd.get_value(obj,'price_floor'))
        price_ceiling = float(gridlabd.get_value(obj,'price_ceiling'))
        PRICE = max(price_floor,min(abs(random.normalvariate(price_mean,price_std)),price_ceiling))
        quantity_mean = float(gridlabd.get_value(obj,'quantity_mean'))
        quantity_std = float(gridlabd.get_value(obj,'quantity_std'))
        quantity_floor = float(gridlabd.get_value(obj,'quantity_floor'))
        quantity_ceiling = float(gridlabd.get_value(obj,'quantity_ceiling'))
        QUANTITY = max(quantity_floor,min(abs(random.normalvariate(quantity_mean,quantity_std)),quantity_ceiling))
        MARGINALTYPE = ('seller' if random.normalvariate(0,1)>0 else 'buyer')
        MARGINALORDER = guid()
        MARGINALQUANTITY = abs(random.normalvariate(5,1))
        MARGINALRANK = int(random.randrange(0,1000))
        gridlabd.set_value(obj, 'auction_id', str(AUCTIONID))
        gridlabd.set_value(obj, 'price', str(PRICE))
        gridlabd.set_value(obj, 'quantity', str(QUANTITY))
        gridlabd.set_value(obj, 'marginal_type', MARGINALTYPE)
        gridlabd.set_value(obj, 'marginal_order', MARGINALORDER)
        gridlabd.set_value(obj, 'marginal_quantity', str(MARGINALQUANTITY))
        gridlabd.set_value(obj, 'marginal_rank', str(MARGINALRANK))
        verbose(f"({dt.datetime.fromtimestamp(t)}) {obj} auction {AUCTIONID} cleared at {dt.datetime.fromtimestamp(MARKETTIME)}")

        # save result into auctions table
        DATABASE.insert_auctions(guid(),AUCTIONID,MARKETTIME,gridlabd.get_value(obj,'resource_id'),PRICE,QUANTITY,MARGINALTYPE,MARGINALORDER,MARGINALQUANTITY,MARGINALRANK)
    return int(t/interval+1)*interval

def auction_postsync(obj,t):
    debug(f"obj={obj}, t={dt.datetime.fromtimestamp(t)}")
    auction = gridlabd.get_object(obj)
    interval = int(auction["interval"])
    ts = timestep(t,interval,1)
    if 1 < ts-t < interval:
        verbose(f"({dt.datetime.fromtimestamp(t)}) {obj} entering realtime at {dt.datetime.fromtimestamp(t)}...")
        gridlabd.set_global("show_progress","FALSE")
    return ts

#
# Devices
#

def device_init(obj,t):
    devices.create(obj,t)
    return 0

def device_precommit(obj,t):
    debug(f"obj={obj}, t={dt.datetime.fromtimestamp(t)}")
    device = gridlabd.get_object(obj)
    if not "parent" in device.keys(): # only devices having a parent can be considered
        return gridlabd.NEVER
    agentid = device["parent"]
    agent = gridlabd.get_object(agentid)
    if not agent["class"] == "agent":
        raise Exception("device parent is not an agent")

    # run bidding strategies for each upcoming market
    for market_type in ["storage","constraint"]:

        # check dispatch for each current market
        last_auctionid = device[f"{market_type}_auctionid"]
        if last_auctionid != '0':
            default_dispatch(device,last_auctionid,market_type)

        # process order if needed
        next_auctionid, resource_id = get_resource_market(agent,market_type)
        if next_auctionid > last_auctionid:
            DEFAULT_STRATEGY[device["type"]](device,resource_id,next_auctionid,market_type)

    return gridlabd.NEVER

def device_commit(obj,t):
    if t%60 == 0:
        cost = 0
        for resource_type in ["power","energy"]:
            order_id = gridlabd.get_value(obj,f'{resource_type}_order').strip('"')
            quantity = float(gridlabd.get_value(obj,f'{resource_type}_quantity').split()[0])
            price = float(gridlabd.get_value(obj,f'{resource_type}_price').split()[0])
            cost += quantity*price/60
        if cost != 0 and order_id != "":
            DATABASE.replace_settlements(record_time=gridlabd.get_global('clock'),order_id=order_id,cost=cost)
    return gridlabd.NEVER

#
# Device-specific bidding strategies
#

def hvac_bid(device,resource_id,auction_id,market_type):
    unit = dict(constraint="power",storage="energy")[market_type]
    quantity = float(device[f"{unit}_quantity"].split()[0])
    price = float(device[f"{unit}_price"].split()[0])
    state = random.normalvariate(quantity,quantity/100)
    flexible = ("NONE").index(device["flexible"])
    if quantity != 0.0 and random.randrange(0,100) < 5:
        submit_order(device['name'],resource_id,auction_id,quantity,price,flexible,state,market_type)

def hotwater_bid(device,resource_id,auction_id,market_type):
    unit = dict(constraint="power",storage="energy")[market_type]
    quantity = float(device[f"{unit}_quantity"].split()[0])
    price = float(device[f"{unit}_price"].split()[0])
    state = random.normalvariate(quantity,quantity/100)
    flexible = ("NONE").index(device["flexible"])
    if quantity != 0.0 and random.randrange(0,100) < 5:
        submit_order(device['name'],resource_id,auction_id,quantity,price,flexible,state,market_type)

def charger_bid(device,resource_id,auction_id,market_type):
    unit = dict(constraint="power",storage="energy")[market_type]
    quantity = float(device[f"{unit}_quantity"].split()[0])
    price = float(device[f"{unit}_price"].split()[0])
    state = random.normalvariate(quantity,quantity/100)
    flexible = ("NONE","POWER","ENERGY","POWER|ENERGY").index(device["flexible"])
    if quantity != 0.0 and random.randrange(0,100) < 5:
        submit_order(device['name'],resource_id,auction_id,quantity,price,flexible,state,market_type)

def battery_bid(device,resource_id,auction_id,market_type):
    unit = dict(constraint="power",storage="energy")[market_type]
    quantity = float(device[f"{unit}_quantity"].split()[0])
    price = float(device[f"{unit}_price"].split()[0])
    state = random.normalvariate(quantity,quantity/100)
    flexible = ("NONE","ENERGY").index(device["flexible"])
    if quantity != 0.0 and random.randrange(0,100) < 5:
        submit_order(device['name'],resource_id,auction_id,quantity,price,flexible,state,market_type)

def solar_bid(device,resource_id,auction_id,market_type):
    unit = dict(constraint="power",storage="energy")[market_type]
    quantity = float(device[f"{unit}_quantity"].split()[0])
    price = float(device[f"{unit}_price"].split()[0])
    state = random.normalvariate(quantity,quantity/100)
    flexible = ("NONE","POWER").index(device["flexible"])
    if quantity != 0.0 and random.randrange(0,100) < 5:
        submit_order(device['name'],resource_id,auction_id,quantity,price,flexible,state,market_type)

DEFAULT_STRATEGY = {
    "HC" : hvac_bid,
    "HW" : hotwater_bid,
    "PV" : solar_bid,
    "EV" : charger_bid,
    "ES" : battery_bid,
}

def default_dispatch(device,auction_id,market_type):
    unit = dict(constraint="power",storage="energy")[market_type]
    quantity = device[f"{unit}_quantity"].split()[0]
    dispatch = device[f"{unit}_dispatch"].split()[0]
    if quantity != 0 and dispatch != quantity:
        try:
            DATABASE.insert_dispatches(gridlabd.get_global('clock'),auction_id,quantity)
        except:
            pass
        finally:
            gridlabd.set_value(device['name'],f"{unit}_dispatch",quantity)            

#
# Bidding utilities
#

def get_resource_market(agent,resource_type):
    auction_id = agent[f"{resource_type}_auction"]
    auction = gridlabd.get_object(auction_id)
    next_auctionid = str(int(auction["auction_id"])+1)
    resource_id = auction['resource_id']
    return next_auctionid, resource_id

def submit_order(obj,resource_id,auction_id,quantity,price,flexible,state,market_type):
    verbose(f"{obj} orders {quantity:.3f} at {price:.2f} from {resource_id} in auction {auction_id}")
    order_id = guid()
    DATABASE.replace_orders(gridlabd.get_global('clock'),order_id,obj,resource_id,auction_id,quantity,price,flexible,state)
    meter_id = guid()
    DATABASE.insert_meter(meter_id,obj,real_power=quantity);
    unit = dict(constraint="power",storage="energy")[market_type]
    gridlabd.set_value(obj,f"{unit}_order",order_id)
    gridlabd.set_value(obj,f"{market_type}_auctionid",auction_id)

