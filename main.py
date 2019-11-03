import pandas as pd
import math

def parse_loc(name_of_city, name_of_country):
    df = pd.read_csv('worldcities.csv', sep=",", usecols=["city_ascii", "lat", "lng", "country"])
    try:
        x_0 = df[df['city_ascii'] == name_of_city]
        y_0 = df[df['city_ascii'] == name_of_city]
        x = float(x_0[x_0['country'] == name_of_country]['lat'])
        y = float(y_0[y_0['country'] == name_of_country]['lng'])
    except:
        print("Does not exist")
    else:
        return x, y

def haversine_formula(pnt_1, pnt_2):
    R = 6371 #earth's radius (km)
    try:
        a = math.sin((math.radians(pnt_1[0])-math.radians(pnt_2[0]))/2)**2
        b = math.cos(math.radians(pnt_1[0])) * math.cos(math.radians(pnt_1[0]))
        c = math.sin((math.radians(pnt_1[1])-math.radians(pnt_2[1]))/2)**2
        e = a + b*c
        d = 2*math.atan2(math.sqrt(e), math.sqrt(1-e))
    except TypeError:
        print("TypeError")
    else:
        return round(R * d, 1)


if __name__ == '__main__':
    pnt_1 = parse_loc("Bishkek", "Kyrgyzstan")
    pnt_2 = parse_loc("Moscow", "Russia")
    print(haversine_formula(pnt_1, pnt_2), "km")