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

#/get/actual?resource_id=<id>
# TODO: now-12hours, Order
# choose name to rerender
# use resource id
# limit 144
@app.route('/get/actual')
def get_actual_value():
    resource_id = request.args.get('resource_id')
    # now - 12 hours
    cur = get_db().cursor().execute(f"""
            SELECT meters.valid_at AS x, sum(meters.real_power) AS y
            FROM meters JOIN devices ON meters.device_id = devices.device_id
            JOIN agents ON devices.agent_id = agents.agent_id
            WHERE agents.resource_id = (?)
            GROUP BY round(meters.valid_at/300)
            (ORDER BY) 
            ;
        """, (resource_id,))

    rv = cur.fetchall()
    return str(rv)

# TODO: now-12hours, Order
# use resource id
@app.route('/get/cleared')
def get_cleared_value():
    # what reported in the auction table
    resource_name = request.args.get('name')
    cur = get_db().cursor().execute(f"""
        SELECT dispatches.valid_at AS x, sum(dispatches.quantity) AS y
        FROM dispatches JOIN orders ON dispatches.order_id = orders.order_id
        JOIN resources ON orders.resource_id = resources.resource_id
        WHERE resources.name = (?)
        GROUP BY round(dispatches.valid_at/300);
            """, (resource_name, ))
    return cur.fetchall()

if __name__ == "__main__":
    app.run(debug=True)
