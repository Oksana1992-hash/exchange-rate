from tkinter import ttk
import requests
import json
from tkinter import *
from tkinter import messagebox as mb


def exchange():
    code = combobox.get() # получить из выпадающего списка то, что ввел пользователь

    if code: # если код есть:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD') # запрос в интернете по сайту
            response.raise_for_status()
            data = response.json() # в переменной получен ответ в формате json
            if code in data['rates']: # если внутри rates есть введенная валюта
                exchange_rate = data['rates'][code] # в переменной окажется курс валюты, который мы искали
                mb.showinfo('Курс обмена', f'Курс: {exchange_rate:.2f} {code} за 1 доллар')
            else:
                mb.showerror('Ошибка', f'Валюта "{code}" не найдена')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}.')
    else: # если пользователь ничего не ввел
        mb.showwarning('Внимание!', 'Введите код валюты')


window = Tk()
window.title('Курсы обмена валюты')
window.geometry('360x180')

Label(text='Выберите код валюты').pack(padx=10, pady=10)

cur = ['RUB', 'EUR', 'GBP', 'JPY', 'CNY', 'KZT', 'UZS', 'CHF', 'AED', 'CAD']
combobox = ttk.Combobox(values=cur)
combobox.pack(padx=10, pady=10)

# entry = Entry()
# entry.pack(padx=10, pady=10)

Button(text='Получить курс обмена к доллару', command=exchange).pack(padx=10, pady=10)

window.mainloop()