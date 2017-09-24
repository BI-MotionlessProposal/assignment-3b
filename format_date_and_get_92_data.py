import pandas as pd
import math
import os



#
# def get_coordinates(filename):
#     df = pd.read_csv(filename, names = ["address","zip_code","price","sell_date","sell_type","price_per_sq_m","no_rooms","housing_type","size_in_sq_m","year_of_construction","price_change_in_pct","aktuel_vardi","street","housenumber","postcode","lat","long"])
#     for index, row in df.iterrows():
#         street = df['street']
#         housenumber = df ['housenumber']
#         postcode = df ['postcode']
#         address = street+housenumber
#         print(address)
#         latitude, longitude = get_locations(address, postcode)
#         df['lat'] = latitude
#         df['long'] = longitude
#     df.to_csv('coordinates.csv')
#
#
# def get_locations(address, zip_code):
#     try:
#         # This removes information about a flats storey
#         address_field = address.split(', ')[0]
#         # This one removes trailing letters on the city name
#         # It seems as if Openstreetmap cannot handle København H
#         # but it works with København
#         zip_field = ' '.join(zip_code.split(' ')[:-1])
#         search_address = ', '.join([address_field, zip_field])
#
#         geolocator = Nominatim()
#         location = geolocator.geocode(search_address)
#         return location.latitude, location.longitude
#     except:
#         print('Skipped geocoding of {} {}'.format(address, zip_code))
#         return None, None


def convert_date(filename):
    df = pd.read_csv('./data/'+filename)
    df['sell_date'] = pd.to_datetime(df['sell_date'],format="%d-%m-%Y")
    df.to_csv(filename+'-date_formatted.csv')

def get_92_data(filename):

    df = pd.read_csv(filename)
    df = df[(df['sell_date'] > '1992-01-01') & (df['sell_date'] < '1992-12-31')]
    df.to_csv(filename+'-dated.csv')

def run_magic():
    for file in os.listdir("./data"):
        if file.endswith(".csv"):
            convert_date(file.title())





def haversine_distance(origin, destination):

    lat_orig, lon_orig = origin
    lat_dest, lon_dest = destination
    radius = 6371

    dlat = math.radians(lat_dest-lat_orig)
    dlon = math.radians(lon_dest-lon_orig)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat_orig))
        * math.cos(math.radians(lat_dest)) * math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d

if __name__ == '__main__':
    run_magic()
    get_92_data('1050-1549.csv-date_formatted.csv')
    get_92_data('5000.csv-date_formatted.csv')
    get_92_data('8000.csv-date_formatted.csv')
    get_92_data('9000.csv-date_formatted.csv')
