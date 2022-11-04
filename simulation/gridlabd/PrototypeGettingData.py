import sqlite3
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
