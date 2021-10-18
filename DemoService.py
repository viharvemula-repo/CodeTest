import json
from flask import Flask, request
from sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine('sqlite:///C:/Users/vihar/demo.db', echo=False)


def get_query(args):
    base_query = "select distinct Location from locations"
    where = 'where'
    if args:
        for i in args:
            if args.get(i) != "":
                if where == 'where':
                    where = where + ' %s = "%s"' % (i, args.get(i))
                else:
                    where = where + ' and %s = "%s"' % (i, args.get(i))
    else:
        return base_query
    return "select * from locations " + where


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/location/", methods=['GET', 'POST'])
def get_locations():
    if request.method == 'GET':
        args = request.args
    if request.method == 'POST':
        args = request.form
    query = get_query(args)
    print(query)
    with engine.connect() as con:
        res = con.execute(query)
        return json.dumps([dict(r) for r in res])


if '__main__' == __name__:
    app.run(debug=True)
