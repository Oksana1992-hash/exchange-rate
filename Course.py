from tkinter import *
from tkinter import ttk
import requests
import json


def generation_list_rates():
    answer = requests.get(f'https://open.er-api.com/v6/latest/RUB')
    json_info = answer.json()
    list_currency = list(json_info['rates'].keys())
    return list_currency

def func_exchange():
    code_target = combo_to.get().upper()
    code_base = combo_from.get()
    if code_target and code_base:
        answer = requests.get(f'https://open.er-api.com/v6/latest/{code_base}')
        json_info = answer.json()
        if code_target in json_info['rates']:
            rez =  json_info['rates'][code_target]
            content_l.config(text=f'1{code_base} - {rez}{code_target}')
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

t_m = Label(text='Выберите код исходной валюты:')
t_m.pack(pady = [10, 10])

combo_from = ttk.Combobox(values=sp_curen)
combo_from.pack(pady = [10, 10])

t_m = Label(text='Выберите код конечной валюты:')
t_m.pack(pady = [10, 10])

combo_to = ttk.Combobox(values=sp_curen)
combo_to.pack(pady = [10, 10])

content_l = Label()
content_l.pack(pady = [10, 10])

btn = Button(text='Конвертировать валюту', command=func_exchange)
btn.pack(pady = [10, 10])



window.mainloop()
