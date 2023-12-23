from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
import requests


#initialize window
root = Tk()
root.title("Weather App")
root.geometry("720x400+300+100")
root.config(bg="#1ab5ef")
root.resizable(False,False)

def getweather() :
    try:
        city  = textfield.get()
    #   city = StringVar()
        geolocator = Nominatim(user_agent="http")
        print(geolocator)
        location = geolocator.geocode(city)
        print(location)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        timezone.config(text=result)
        long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")
    
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%d-%m-%y    %H:%M%p")
        name.config(text="Current Date&Time")
        clock.config(text=current_time)
    
        #weather
        
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=2a55d9200bcc7d233bf1237d8a2e2884"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        # cloud = json_data['clouds']['all']
    
        t.config(text=(temp, "°c"))
        w.config(text=(wind, "mi/h"))
        h.config(text=(humidity, "%"))
        d.config(text=description)   
        # c.config(text=(cloud, "%")) 
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!")

def text_enter(e):
    textfield.delete(0, 'end')
    
def text_leave(e):
    t1 = textfield.get()
    if t1=='':
        textfield.insert(0,'Search here')
    
    
        
# Searchbox
search_image = PhotoImage(file="Rounded Rectangle 3.png")
myimage = Label(image=search_image, bg="#57adff")
myimage.place(x=30, y=50)

search_icon = PhotoImage(file="Layer 6.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#203243", activebackground="#20374d", command=getweather)
myimage_icon.place(x=407, y=55)


textfield =  tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg="#203243", border=0, fg="white")
textfield.insert(0, 'Search here')
textfield.bind("<FocusIn>", text_enter)
textfield.bind("<FocusOut>", text_leave)
textfield.place(x=120, y=60)
# textfield.focus()


# #logo
# weather_logo = PhotoImage(file="weather.png")
# Label(root, image=weather_logo, borderwidth=-1).place(x=480, y=0)

#time
name = Label(root, font=("arial", 15, "bold"), fg="white", bg="#1ab5ef")
name.place(x=300, y=140)
clock = Label(root,font=("Helvetica", 11, "bold"), fg="white", bg="#1ab5ef")
clock.place(x=300, y=170)


# #BottomBox
frame = Frame(root, bg="#212120", height=150, width=720)
frame.pack(side=BOTTOM)

t_label = Label(root,fg="white", bg="#1ab5ef", text="Temp", font=("Helvetica", 15, "bold"))
t_label.place(x=70, y=280, height=40, width=120)
t = Label(root, text=". . . . .", font=("Helvetica", 11, "bold"), fg="white", bg="#212120")
t.place(x=100, y=350)

w_label = Label(root,fg="white", bg="#1ab5ef", text="Wind", font=("Helvetica", 15, "bold"))
w_label.place(x=220, y=280, height=40, width=120)
w = Label(root, text=". . . . .", font=("Helvetica", 11, "bold"), fg="white", bg="#212120")
w.place(x=250, y=350)

h_label = Label(root,fg="white", bg="#1ab5ef", text="Humidity", font=("Helvetica", 15, "bold"))
h_label.place(x=370, y=280, height=40, width=120)
h = Label(root, text=". . . . .", font=("Helvetica", 11, "bold"), fg="white", bg="#212120")
h.place(x=400, y=350)

d_label = Label(root, fg="white", bg="#1ab5ef", text="Description", font=("Helvetica", 15, "bold"))
d_label.place(x=520, y=280, height=40, width=120)
d = Label(root, text=". . . . .", font=("Helvetica", 11, "bold"), fg="white", bg="#212120")
d.place(x=550, y=350)

# label5 = Label(root, text="Clouds", font=("Helvetica", 11, "bold"), fg="white", bg="#292928")
# label5.place(x=570, y=275)
# c = Label(root, text=". . . . .", font=("Helvetica", 11, "bold"), fg="white", bg="#292928")
# c.place(x=576, y=320)

# timezone
timezone = Label(root, font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
timezone.place(x=100, y=140)

long_lat = Label(root, font=("Helvetica", 11, "bold"), fg="white", bg="#1ab5ef")
long_lat.place(x=100, y=170)

root.mainloop()
