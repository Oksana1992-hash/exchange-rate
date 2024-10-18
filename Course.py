import requests
import json
from tkinter import *


def func_exchange():
    code = e.get().upper()
    if code:
        answer = requests.get('https://open.er-api.com/v6/latest/RUB')
        json_info = answer.json()
        if code in json_info['rates']:
            rez =  json_info['rates'][code]
            content_l.config(text=f'1RUB - {rez}{code}')
            content_l.config(fg='green')
        else:
            content_l.config(text='Такого кода валюты не существует')
            content_l.config(fg='red')
    else:
        content_l.config(text='Код валюты не введен')
        content_l.config(fg='red')






window = Tk()
window.title('Курс валют')
window.geometry('400x400')

e = Entry()
e.pack()

content_l = Label()
content_l.pack()

btn = Button(text='Получить курс рубля', command=func_exchange)
btn.pack()



window.mainloop()
