# uber
Data Mining using Uber API
Uber developer API allows us to download realtime Price and Time estimate for the input location.

This Python code downloads the following data:

Price estimate - Maximum/Minimum Fare, Surge, Distance and Time for various cab options.
Time Estimate - Wait times for a given location and cab options available nearby.
The python code requires a csv file having Start and End locations in the form of Latitude/Longitude.

The data is downloaded in JSON format for every 10 minutes. Try increasing the sleep time to adjust the time difference of data download.

The data can used for making several mobile or web apps to predict surge pricing and Uber service based on demand and supply.
