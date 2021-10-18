import json
from flask import Flask, request
from LocationSKU import LocationSKU
from sqlalchemy import create_engine


from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
engine = create_engine('sqlite:///C:/Users/vihar/demo.db', echo=False)


def get_filter_condition(args):
    form = args.to_dict()
    filters = []
    for col in form:
        filter_expression = (getattr(LocationSKU, col) == form[col])
        filters.append(filter_expression)
    return filters


@app.route("/location_details/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_locations():
    if request.method == 'GET':
        args = request.args
    if request.method == 'POST':
        args = request.form
    filter_condition = get_filter_condition(args)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    res = session.query(LocationSKU).filter(*filter_condition).all()
    output = []
    for r in res:
        del r.__dict__['_sa_instance_state']
        output.append(r.__dict__)
    return json.dumps(output)


@app.route("/delete_sku/", methods=['GET', 'DELETE'])
def delete_sku():
    args = request.args
    filter_condition = get_filter_condition(args)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    session.query(LocationSKU).filter(*filter_condition).delete()
    session.commit()
    return "Record removed successfully"


@app.route("/add_sku/", methods=['PUT', 'OPTIONS'])
def add_sku():
    print(request.method)
    args = request.args
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    new = LocationSKU(args['SKU'], args['Name'], args['Location'], args['Department'], args['Category'], args['SubCategory'])
    session.add(new)
    session.commit()
    return "Record added successfully"


if '__main__' == __name__:
    app.run(debug=True)