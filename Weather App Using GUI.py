from tkinter import *
from tkinter import messagebox
import requests
import json
from configparser import ConfigParser

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']
print(api_key)


def search_weather(city):
    result = requests.get(url.format(city,api_key))
    if result:
        readable = result.json()
        city = readable['name']
        country = readable['sys']['country']
        t_k = readable['main']['temp']
        t_c = int(t_k - 273.15)
        t_f = int(t_c*9/5+32)
        weather = readable['weather'][0]['main']
        final = (city , country , t_c , t_f , weather)
        return final
    else:
        return None


def search():
    city = c_txt.get()
    weather = search_weather(city)
    if weather:
        loc_lbl['text'] = '{},{}'.format(weather[0],weather[1])
        temp_lbl['text'] = '{}°C , {}°F'.format(weather[2],weather[3])
        w_lbl['text'] = '{}'.format(weather[4]) 
    else:
        messagebox.showerror('Error','City not found')
    loc_lbl.pack(pady = 10)
    temp_lbl.pack(pady = 10)
    w_lbl.pack(pady = 10)


root=Tk()
root.title('Weather')
root.configure(bg = 'light blue')
root.geometry('300x300')


c_txt = StringVar()

city_entry = Entry(root, textvariable= c_txt)
city_entry.pack(pady = 10)

search = Button(root, text='Search',command=search)
search.pack(pady = 10)

loc_lbl = Label(root, text = 'Location',font='bold')


temp_lbl = Label(root,text = 'Temprature',font = 'bold')


w_lbl = Label(root,text = 'Weather',font = 'bold')



root.mainloop()

