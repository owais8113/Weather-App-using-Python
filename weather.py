import tkinter as tk
from tkinter import ttk
import datetime
import requests
def data_get():
    city = city_name.get()
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=7631c9b743d92ddd27fc9305060d3f8b"
    data = requests.get(url).json()
    Weather_climate_label1.config(text=data["weather"][0]["main"])    
    temperature_label1.config(text=round((data["main"]["temp"]-273.15),2))
    humidity_label1.config(text=data["main"]["humidity"])
    pressure_label1.config(text=data["main"]["pressure"])
    speed_label1.config(text=data["wind"]["speed"])

window = tk.Tk()
window.title("Weather App")
window.geometry("475x500")
window.minsize(475, 500)
 
# set maximum window size value
window.maxsize(475, 500)
window.configure(bg="#1F1F1F")  # Set dark background color
city_name = tk.StringVar()
city_name.set("")
title_label = tk.Label(window, text="Weather App", font=("Arial", 24, "italic"), fg="#FFFFFF", bg="#1F1F1F")
title_label.pack(pady=20)

location_combobox = ttk.Combobox(window, font=("Arial", 16), width=20, textvariable=city_name)
location_combobox.pack(pady=10)


get_weather_button = tk.Button(window, text="Get Weather", font=("Arial", 16), command=data_get, bd="2px white",bg="#FFFFFF", fg="#1F1F1F")
get_weather_button.pack(pady=10)

speed_label = tk.Label(window, text="Wind Speed(m/s): ", font=("Arial", 16), fg="#FFFFFF", bg="#1F1F1F")
speed_label.place(x= 35,y = 200)
speed_label1 = tk.Label(window, text="", font=("Times New Roman", 16), fg="#FFFFFF", bg="#1F1F1F")
speed_label1.place(x= 250,y = 200)

Weather_climate_label = tk.Label(window, text="Climate: ", font=("Arial", 16), fg="#FFFFFF", bg="#1F1F1F")
Weather_climate_label.place(x= 35,y = 250)
Weather_climate_label1 = tk.Label(window, text="", font=("Times New Roman", 16), fg="#FFFFFF", bg="#1F1F1F")
Weather_climate_label1.place(x= 250,y = 250)

temperature_label = tk.Label(window, text="Temperature(°C): ", font=("Arial", 16), fg="#FFFFFF", bg="#1F1F1F")
temperature_label.place(x= 35,y = 300)
temperature_label1 = tk.Label(window, text="", font=("Times New Roman", 16), fg="#FFFFFF", bg="#1F1F1F")
temperature_label1.place(x= 250,y = 300)

humidity_label = tk.Label(window, text="Humidity(%): ", font=("Arial", 16), fg="#FFFFFF", bg="#1F1F1F")
humidity_label.place(x= 35,y = 350)
humidity_label1 = tk.Label(window, text="", font=("Times New Roman", 16), fg="#FFFFFF", bg="#1F1F1F")
humidity_label1.place(x= 250,y = 350)


pressure_label = tk.Label(window, text="Pressure(mbar): ", font=("Arial", 16), fg="#FFFFFF", bg="#1F1F1F")
pressure_label.place(x= 35,y = 400)
pressure_label1 = tk.Label(window, text="", font=("Times New Roman", 16), fg="#FFFFFF", bg="#1F1F1F")
pressure_label1.place(x= 250,y = 400)

current_time_label = tk.Label(window, text="Current Time: ", font=("Arial", 16), fg="#FFFFFF", bg="#1F1F1F")
current_time_label.place(x= 50,y = 450)

def update_current_time():
    current_time = datetime.datetime.now().strftime(f"%d-%m-%y %H:%M:%S IST")
    current_time_label.config(text="Current Time: " + current_time)
    window.after(1000, update_current_time)  # Update every second

update_current_time()


window.mainloop()
