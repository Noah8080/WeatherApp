
This program uses OpenWeatherMap's API to return the current weather and a forcast for each of the next two days. 
There are unit tests for validating the user's entered zip code and validating the data returned by the API. 
There is a logger to log errors and other program information in 'log.txt'
There is nothing encrypted since there is no data being stored, only outputted to the terminal. 
I used Snyk, a Static code analysis tool that can be used through either GitHub or cli scanning. It found no vulnerabilities with this code. 
The packages used are JSON, Requests, Logging, and unittest. 
