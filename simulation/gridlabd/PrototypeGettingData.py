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


#/get/actual?name=Feeder_1
@app.route('/get/actual')
def get_actual_value():
    resource_name = request.args.get('name')
    cur = get_db().cursor().execute(f"""
            SELECT meters.valid_at AS x, sum(meters.real_power) AS y
            FROM meters JOIN devices ON meters.device_id = devices.device_id
            JOIN agents ON devices.agent_id = agents.agent_id
            JOIN resources ON agents.resource_id = resources.resource_id
            WHERE resources.name = (?)
            group by round(meters.valid_at/300);
        """, (resource_name,))

    rv = cur.fetchall()
    return str(rv)

@app.route('/get/cleared')
def get_cleared_value():
    # what reported in the auction table
    cur = get_db().cursor().execute(f"""
            SELECT quantity, market_time FROM auctions 
            WHERE market_time > (?)
            ORDER BY market_time;
            """, (datetime.datetime.now() - datetime.timedelta(hours=24)))
    return cur.fetchall()


@app.route('/get/settingsValue')
def get_settings_value():
    # here we want to get the value of name (i.e. ?name=some-value)
    name = request.args.get('name')
    print("Name: ", name)
    cur = get_db().cursor().execute(f"""
        select value
        from settings
        where name = (?)
        order by value_at desc;
        """, (name,))

    rv = cur.fetchall()
    return rv


@app.route('/get/markets_resourceid_units_interval')
def get_markets_resourceid_units_interval():
    cur = get_db().cursor().execute(f"""
        select resource_id, units, interval 
        from markets;
        """)

    rv = [dict((cur.description[agent_id][0], resource_id) for agent_id, resource_id in enumerate(row)) for row in
          cur.fetchall()]
    return rv


@app.route('/get/auctions_markettime_resourceid_quantity_price_auctionid')
def get_auctions_markettime_resourceid_quantity_price_auctionid():
    # here we want to get the value of market_id (i.e. ?market_id=some-value)
    market_id = int(request.args.get('market_id'))
    print("Market Id: ", market_id)
    cur = get_db().cursor().execute(f"""
           select market_time, resource_id, quantity, price, auction_id 
        from auctions 
        where market_id = (?)
        order by resource_id;
           """, (market_id,))

    rv = cur.fetchall()
    return rv


@app.route('/get/load')
def get_auction_pv():
    status = request.args.get('status', default = 'all', type = str)
    device_type = request.args.get('device_type', default = 'all', type = str)
    if (status == 'dispatched'):
        cur = get_db().cursor().execute(f"""SELECT * FROM agents;""")
    elif (status == 'available'):
        return 'available'
    elif (status == 'unavailable'):
        return 'unavailable'
    elif (status == 'all'):
        return 'all'
    else:
        return 'WRONG STATUS!!'     

    cur = get_db().cursor().execute(f"""SELECT * FROM agents;""")
    rv = cur.fetchall()
    return str(rv)

if __name__ == "__main__":
    app.run(debug=True)
