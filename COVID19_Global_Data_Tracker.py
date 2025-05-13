import tkinter as tk
import requests
import datetime

def getCovidData():
    api = "https://disease.sh/v3/covid-19/all"
    return api

api = getCovidData()  # Call the function to assign api
json_data = requests.get(api).json() #requesting to get the above API data through JSON file
total_cases = str(json_data['cases']) #assigning total cases as mentioned in the api
total_deaths = str(json_data['deaths']) #assigning total deaths as mentioned in the api
today_cases = str(json_data['todayCases']) #assigning today cases as mentioned in the api
today_deaths = str(json_data['todayDeaths']) #assigning total deaths as mentioned in the api
today_recovered = str(json_data['todayRecovered']) #assigning today recovered as mentioned in the api
updated_at = json_data['updated'] #used to update the given details using time
date = datetime.datetime.fromtimestamp(updated_at/1e3)

# Create the main window
root = tk.Tk() 
root.title("Covid-19 Tracker") # Setting title for the window
root.geometry("400x300") # Setting the size of the window
root.configure(bg="lightblue") # Setting the background color of the window
# Create a label widget
label = tk.Label(root, text="") # Initializing label and Keeping text empty before updating from API
label.pack() # Making the label visible by packing it

# retrieving the details from API and displaying the results in Tkinter
label.config(text="Total Cases: " + total_cases +
                "\n" + "Total Deaths: " + total_deaths +
                "\n" + "Today Cases: " + today_cases +
                "\n" + "Today Deaths: " + today_deaths +
                "\n" + "Today Recovered: " + today_recovered)


root.mainloop() # Start the Tkinter event loop to keep the window open