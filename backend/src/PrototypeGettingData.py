import sqlite3
from datetime import datetime, timedelta

import datetime
from flask import g, Flask
from flask import request

app = Flask(__name__)

DATABASE = 'gridlabd.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# TODO
###
#select distinct(resource_id), valid_at from resources order by valid_at;
#

# [resource_id] --> get [name] from most recent valid_at --> front end build drop down from [name]-->new query
# [resource_id, current_name]
# page, limit (20)
# optional argument, last_resource_id
# order return value yb resource id, return next 20 values greater than last_resource_id


@app.route('/get/resources')
def get_all_resources():
    cur = get_db().cursor().execute(f"""
            SELECT resource_id from resources;
        """)
    rv = cur.fetchall()
    return str(rv)

# DEPRECATED
# /get/actual?resource_id=<id>
# TODO: now-12hours, Order
# choose name to rerender
# use resource id

# load, storage: different queries by arg
# load/power:interval 60 limit 720,
#@app.route('/get/actual_power'): GROUP BY round(meters.valid_at/60)

# storage/energy: interval 300 limit 144
#@app.route('/get/actual_energy') : GROUP BY round(meters.valid_at/300)
@app.route('/get/actual_power')
def get_actual_value():
    resource_id = request.args.get('resource_id') #market_id --> each resource has two markets
    # now - 12 hours
    cur = get_db().cursor().execute(f"""
            SELECT meters.valid_at AS x, sum(meters.real_power) AS y
            FROM meters JOIN devices ON meters.device_id = devices.device_id
            JOIN agents ON devices.agent_id = agents.agent_id
            WHERE agents.resource_id = (?)
            GROUP BY round(meters.valid_at/60)
            ;
        """, (resource_id,))

    rv = cur.fetchall()
    return str(rv)

# TODO: now-12hours, Order
# use resource id
# now - 12 hours
# market interval 60 limit 720 ---> power
# market interval 300 limit 144 --> energy
# order by 'x'
# use market_id
# can get negative quantity*
@app.route('/get/cleared')
def get_cleared_value():
    # what reported in the auction table
    market_id = request.args.get('market_id')
    cur = get_db().cursor().execute(f"""
        SELECT dispatches.valid_at AS x, sum(dispatches.quantity) AS y
        FROM dispatches JOIN orders ON dispatches.order_id = orders.order_id
        JOIN auctions ON auctions.order_id = orders.order_id
        WHERE auctions.market_id = (?)
        GROUP BY round(dispatches.valid_at/300 - 0.5)
        ORDER BY dispatches.valid_at DESC
        LIMIT 144;
            """, (market_id, ))
    return cur.fetchall()

# available
### update every 5 (300) mins
# 'now'
# open_time = ROUND(now/300 - 0.5) * 300
# one device supports only one market
#
# CURRENT_TIMESTAMP

# SELECT devices.device_type as x, SUM(orders.quantity) as y
# FROM orders 
# JOIN devices ON orders.device_id = devices.device_id 
# GROUP BY devices.device_type
# WHERE orders.valid_at >= open_time ###


if __name__ == "__main__":
    app.run(debug=True)
