from geocoder import ip
from requests import get
from datetime import datetime


units = "metric"
API = "your_API"
main_url = "http://api.openweathermap.org/data/2.5/"

data = [
    {"": 0, "title": "Monday",    "active": False, "order": (0, 1, 2, 3, 4, 5, 6)},
    {"": 1, "title": "Tuesday",   "active": False, "order": (1, 2, 3, 4, 5, 6, 0)},
    {"": 2, "title": "Wednesday", "active": False, "order": (2, 3, 4, 5, 6, 0, 1)},
    {"": 3, "title": "Thursday",  "active": False, "order": (3, 4, 5, 6, 0, 1, 2)},
    {"": 4, "title": "Friday",    "active": False, "order": (4, 5, 6, 0, 1, 2, 3)},
    {"": 5, "title": "Saturday",  "active": False, "order": (5, 6, 0, 1, 2, 3, 4)},
    {"": 6, "title": "Sunday",    "active": False, "order": (6, 0, 1, 2, 3, 4, 5)}
]


def week():
    sequence = tuple()

    today = datetime.today()  # the current time in your system
    data[today.weekday()]["active"] = True  # day of the week (today)

    # searching the current sequence
    for _ in data:
        if data[today.weekday()]["active"]:
            sequence = (data[today.weekday()]["order"])
            break

    # getting your coordinates
    coordinates = ip('me')
    # city = coordinates.city
    lati = coordinates.lat
    long = coordinates.lng

    # main request to server
    req = get(f"{main_url}onecall?/exclude=daily&lat={lati}&lon={long}&appid={API}&units={units}").json()

    days = [data[day] for day in sequence]
    for day in req["daily"]:
        index = req["daily"].index(day)
        if index == 7:
            break

        if days[index]["active"]:
            days[index]["temp"] = day["temp"]["day"]
            days[index]["temp_night"] = day["temp"]["night"]
            days[index]["temp_eve"] = day["temp"]["eve"]
            days[index]["temp_morn"] = day["temp"]["morn"]
            days[index]["type"] = day["weather"][0]["description"]
            days[index]["wind_speed"] = day["wind_speed"]
            days[index]["pressure"] = day["pressure"]
            days[index]["moon_phase"] = day["moon_phase"]
        else:
            days[index]["temp"] = day["temp"]["day"]
            days[index]["type"] = day["weather"][0]["description"]
            days[index]["wind_speed"] = day["wind_speed"]
            days[index]["pressure"] = day["pressure"]

    return days


# res = week()
# for i in res:
#     print(i)
