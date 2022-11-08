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

@app.route('/get/resources')
def get_all_resources():
    cur = get_db().cursor().execute(f"""
            SELECT name from resources;
        """)
    rv = cur.fetchall()
    return str(rv)

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
