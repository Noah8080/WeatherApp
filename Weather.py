def main():
    # store weather api key
    key = "946ee54bb057c38d12d8ed13c2e4ca74"

    import requests
    import datetime

    # get user zip
    zip_code = int(input("Enter a ZipCode: "))
    # make sure a 5 digit code is entered
    if zip_code < 0 or zip_code > 99999:
        print("Please enter a five digit zipcode")
        exit()

    # make the request
    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?q={zip_code},US&units=imperial&APPID={key}")
    # store the results
    forcast = data.json()

    # get present forcast
    day = 0
    get_current_weather(forcast, day)

    # store the date of the current forcast
    date = parse_date(forcast, day)

    # find the index at which the date changes to call for a forcast
    i = 0
    if date == check_date(forcast, i):
        while date == check_date(forcast, i):
            # if date from next forcast is the same as the
            # current forcast, go to next index
            i += 1
        print("---------")
        # once they aren't the same request data
        # from forcast with a new date
        get_future_forcast(forcast, i)

        # saves date of tomorrow's forcast
        next_date = check_date(forcast, i)

        while next_date == check_date(forcast, i):

            i += 1
        print("---------")
        # gets forcast from two days out
        get_future_forcast(forcast, i)


def get_current_weather(forcast, day):
    city = forcast['city']['name']
    date = parse_date(forcast, day)
    print("In " + city + " on " + date)

    temp = round(forcast['list'][0]['main']['temp'])
    temp = str(temp)
    print("The temp is " + temp + " ºF")

    weather_type = forcast['list'][0]['weather'][0]['description']
    print("The condition is " + weather_type)

    wind = round(forcast['list'][0]['wind']['speed'])
    wind = str(wind)
    print("The wind is blowing at " + wind + " mph")


def get_future_forcast(forcast, i):
    hld = i
    city = forcast['city']['name']
    date = check_date(forcast, hld)
    print("In " + city + " on " + date)

    temp = round(forcast['list'][hld]['main']['temp'])
    temp = str(temp)
    print("The temp is " + temp + " ºF")

    weather_type = forcast['list'][hld]['weather'][0]['description']
    print("The condition is " + weather_type)

    wind = round(forcast['list'][hld]['wind']['speed'])
    wind = str(wind)
    print("The wind is blowing at " + wind + " mph")


def parse_date(forcast, day):
    # gets the date from the day the forcast was requested
    date = forcast['list'][day]['dt_txt']
    # remove the time from the end of the date field
    cur_date = date[0:10]
    return cur_date


def check_date(forcast, i):
    # get date from future forcast to find change in date
    d = forcast['list'][i]['dt_txt']
    cd = d[0:10]
    return cd


if __name__ == '__main__':
    main()
