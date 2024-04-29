

def main():
    import requests
    import datetime
    import secrets1
    import logging
    
    
    # set up logging
    logging.basicConfig(filename='weather.log', level=logging.INFO, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
    
    
    # get the api  (from openweathermap.org)
    try:
        key = secrets1.secrets()
        logging.info("Key retrieved")
    except KeyError as e:
        logging.exception("Error getting key")
        print("Error getting key")
        exit()
        

    # get user zip
    try:
        zip_code = int(input("Enter a ZipCode: "))
    except ValueError as e:
        print("Please enter a 5 digit zipcode")
        logging.error("Invalid input")
        exit()
    
    # check for valid length of input
    is_five_digits(str(zip_code))
    
    bruh = 1

    try:
        # make the request
        data = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?q={zip_code},US&units=imperial&APPID={key}")
        # store the returned data
        forcast = data.json()
        # check if the retured data is for a valid city
        get_cod(forcast)
    except:
        print("Request failed")
        print(forcast)
        exit()
        
    # get present forcast
    day = 0
    try:
        get_current_weather(forcast, day)
    except:
        print("Error getting current forcast, invalid data returned.")
        exit()

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
        
        
'''make sure entered num is five digits'''
def is_five_digits(zip_code):
    if len(zip_code) != 5:
        print("Please enter a 5 digit zipcode")
        exit()

'''make sure the entered zip code returns data'''
def get_cod(forcast):
    cod = forcast['cod']
    sanitize(cod)
    if cod == '404' or cod == '':
        print("City not found! Please enter a valid zipcode!")
        logging.error("Zip code does not contain city information")
        exit()

'''gets the current weather forcast. Location, date, temp, weather type, and wind speed'''
def get_current_weather(forcast, day):
    
    # get the city and date, sanatize them, and print them
    city = forcast['city']['name']
    sanitize(city)
    date = parse_date(forcast, day)
    sanitize(date)
    print("In " + city + " on " + date)

    # get the temp, round it, convert to a string, sanatize it, and print it
    temp = round(forcast['list'][0]['main']['temp'])
    temp = str(temp)
    sanitize(temp)
    print("The temp is " + temp + " ºF")

    # get the weather type, sanatize it, and print it
    weather_type = forcast['list'][0]['weather'][0]['description']
    sanitize(weather_type)
    print("The condition is " + weather_type)

    # get the wind speed, round it, convert to a string, sanatize it, and print it
    wind = round(forcast['list'][0]['wind']['speed'])
    wind = str(wind)
    sanitize(wind)
    print("The wind is blowing at " + wind + " mph")

'''gets the future forcast, i is the index of tomorrow's date'''
def get_future_forcast(forcast, i):
    
    # get the city and date, sanatize them, and print them
    city = forcast['city']['name']
    date = check_date(forcast, i)
    sanitize(city)
    sanitize(date)
    print("In " + city + " on " + date)

    # get the temp, round it, convert to a string, sanatize it, and print it
    temp = round(forcast['list'][i]['main']['temp'])
    temp = str(temp)
    sanitize(temp)
    print("The temp is " + temp + " ºF")

    # get the weather type, sanatize it, and print it
    weather_type = forcast['list'][i]['weather'][0]['description']
    sanitize(weather_type)
    print("The condition is " + weather_type)

    # get the wind speed, round it, convert to a string, sanatize it, and print it
    wind = round(forcast['list'][i]['wind']['speed'])
    wind = str(wind)
    sanitize(wind)
    print("The wind is blowing at " + wind + " mph")

'''gets the date from the day the forcast was requested'''
def parse_date(forcast, day):
    date = forcast['list'][day]['dt_txt']
    # remove the time from the end of the date field
    cur_date = date[0:10]
    return cur_date

'''gets the date from the forcast at index i'''
def check_date(forcast, i):
    d = forcast['list'][i]['dt_txt']
    cd = d[0:10]
    return cd


'''Sanitize the input to prevent SQL injection attacks'''
# storing results to a database could be added in the future
def sanitize(input):
    # Blacklist SQL keywords
        input = input.replace("SELECT","")
        input = input.replace("DELETE","")
        input = input.replace("DROP","")
        input = input.replace("%","")
        input = input.replace("*", "")
        input = input.replace("=", "")
        return input


if __name__ == '__main__':
    main()