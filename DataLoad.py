import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///C:/Users/vihar/demo.db', echo=False)
location_path = r"C:\Users\vihar\Desktop\Test Demo\Input\Locations.csv"
location_sku_path = r"C:\Users\vihar\Desktop\Test Demo\Input\SKU.csv"

#pd.read_csv(r"C:\Users\vihar\Desktop\Test Demo\Input\Locations.csv").to_sql('locations', con=engine)

#pd.read_csv(r"C:\Users\vihar\Desktop\Test Demo\Input\SKU.csv").to_sql('locations_details', con=engine)


def csv_loader(path, table_name):
    pd.read_csv(path).to_sql(table_name, con=engine)


def get_data():
    with engine.connect() as con:
        rs = con.execute("select * from locations_dummy")
        for row in rs:
            print(row)


if '__main__' == __name__:
    csv_loader(location_path, 'locations_dummy')
    #get_data()