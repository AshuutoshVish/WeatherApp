#waether forecasting App
from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=ca2b656f9f5e40551d7ef33644df5f46").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    t_label1.config(text=int(data["main"]["temp"]-273.15))
    temp_label1.config(text=int(data["main"]["temp_min"]-273.15))
    tempmx_label1.config(text=int(data["main"]["temp_max"]-273.15))
    p_label1.config(text=data["main"]["pressure"])
    

win=Tk()
win.config(bg='white')
win.geometry("415x500")
name_label=Label(win, text="Weather App",
                 font=("Time New Roman",27,"bold"))
name_label.place(x=70,y=30,height=55,width=280)


city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com= ttk.Combobox(win,text="Weather App",values=list_name,
                  font=("Time New Roman",15,"bold"),textvariable=city_name)
com.place(x=85,y=100,height=40,width=250)

#weather Climate
w_label=Label(win, text="Weather Climate       : ",
                 font=("Time New Roman",10,"bold"))
w_label.place(x=80,y=200,height=20,width=145)
w_label1=Label(win, text="",
                 font=("Time New Roman",10,"bold"))
w_label1.place(x=235,y=200,height=20,width=110)

#Weather Description
wd_label=Label(win, text="Weather Desciption   : ",
                 font=("Time New Roman",10,"bold"))
wd_label.place(x=80,y=225,height=20,width=145)
wd_label1=Label(win, text="",
                 font=("Time New Roman",10,"bold"))
wd_label1.place(x=235,y=225,height=20,width=110)

#temperature
t_label=Label(win, text="Temperature             : ",
                 font=("Time New Roman",10,"bold"))
t_label.place(x=80,y=250,height=20,width=145)
t_label1=Label(win, text="",
                 font=("Time New Roman",10,"bold"))
t_label1.place(x=235,y=250,height=20,width=110)

#Min temperature
temp_label=Label(win, text="Temperature Min       : ",
                 font=("Time New Roman",10,"bold"))
temp_label.place(x=80,y=275,height=20,width=145)
temp_label1=Label(win, text="",
                 font=("Time New Roman",10,"bold"))
temp_label1.place(x=235,y=275,height=20,width=110)

#Max temperature
tempmx_label=Label(win, text="Temperature Max      : ",
                 font=("Time New Roman",10,"bold"))
tempmx_label.place(x=80,y=300,height=20,width=145)
tempmx_label1=Label(win, text="",
                 font=("Time New Roman",10,"bold"))
tempmx_label1.place(x=235,y=300,height=20,width=110)

#Pressure
p_label=Label(win, text="Pressure                    : ",
                 font=("Time New Roman",10,"bold"))
p_label.place(x=80,y=325,height=20,width=145)
p_label1=Label(win, text="",
                 font=("Time New Roman",10,"bold"))
p_label1.place(x=235,y=325,height=20,width=110)

#Owner
w_label=Label(win, text="Developed By Ashuu",
                 font=("Time New Roman",10,"bold"))
w_label.place(x=120,y=370,height=40,width=160)

#Done Button
done_button=Button(win,text="Done",
                   font=("Time Now Roman",20,"bold"),command=data_get)
done_button.place(x=160,y=145,height=40,width=100)                      
win.mainloop() 