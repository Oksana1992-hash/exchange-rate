from tkinter import *
from tkinter import ttk
import requests
import json


def generation_list_rates():
    list_currency = []
    answer = requests.get('https://open.er-api.com/v6/latest/RUB')
    json_info = answer.json()
    list_currency = list(json_info['rates'].keys())
    return list_currency

def func_exchange():
    code = combo.get().upper()
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

sp_curen = generation_list_rates()


t_m = Label(text='Выберите код валюты:')
t_m.pack(pady = [10, 10])

combo = ttk.Combobox(values=sp_curen)
combo.pack(pady = [10, 10])

content_l = Label()
content_l.pack(pady = [10, 10])

btn = Button(text='Получить курс рубля', command=func_exchange)
btn.pack(pady = [10, 10])



window.mainloop()
