import requests


from tkinter import *
from bs4 import BeautifulSoup
from fake_headers import Headers
from threading import Thread


root = Tk()
root.title("Калькулятор")
root.geometry("265x400")
exp = ""


pole = StringVar()
txt = Entry(textvariable=pole)
txt.grid(columnspan=4, ipadx=70)


def dollar():
    global exp
    req = requests.get("https://www.banki.ru/products/currency/cash/usd/moskva/", headers=Headers().generate()).text
    soup = BeautifulSoup(req, "lxml")
    curse = float(exp) * float(soup.find(class_="Text__sc-j452t5-0 bCCQWi").text.replace("₽", "").replace(",", "."))
    pole.set(round(curse, 1))
    exp = f"{pole.get()}"


def eur():
    global exp
    req = requests.get("https://www.banki.ru/products/currency/eur/", headers=Headers().generate()).text
    soup = BeautifulSoup(req, "lxml")
    curse = float(exp) * float(soup.find(class_="Text__sc-j452t5-0 bCCQWi").text.replace("₽", "").replace(",", "."))
    pole.set(round(curse, 1))
    exp = f"{pole.get()}"


def send(sym):
    global exp
    exp += str(sym)
    pole.set(exp)


def it():
    global exp
    try:
        pole.set(eval(exp))
        exp = f"{pole.get()}"
    except Exception:
        pole.set("Ой, ошибка")


button_one = Button(text="1", height=1, width=11, command=lambda: send("1"))
button_one.grid(row=2, column=0)

button_two = Button(text="2", height=1, width=11, command=lambda: send("2"))
button_two.grid(row=2, column=1)

button_three = Button(text="3", height=1, width=11, command=lambda: send("3"))
button_three.grid(row=2, column=2)

button_four = Button(text="4", height=1, width=11, command=lambda: send("4"))
button_four.grid(row=3, column=0)

button_five = Button(text="5", height=1, width=11, command=lambda: send("5"))
button_five.grid(row=3, column=1)

button_six = Button(text="6", height=1, width=11, command=lambda: send("6"))
button_six.grid(row=3, column=2)

button_seven = Button(text="7", height=1, width=11, command=lambda: send("7"))
button_seven.grid(row=4, column=0)

button_eight = Button(text="8", height=1, width=11, command=lambda: send("8"))
button_eight.grid(row=4, column=1)

button_nine = Button(text="9", height=1, width=11, command=lambda: send("9"))
button_nine.grid(row=4, column=2)

button_add = Button(text="+", height=0, width=11, command=lambda: send("+"))
button_add.grid(row=5, column=0)

button_sub = Button(text="-", height=0, width=11, command=lambda: send("-"))
button_sub.grid(row=5, column=1)

button_mul = Button(text="*", height=0, width=11, command=lambda: send("*"))
button_mul.grid(row=5, column=2)

button_zero = Button(text="0", height=0, width=11, command=lambda: send("0"))
button_zero.grid(row=5, column=1)

button_eq = Button(text="=", height=0, width=11, command=lambda: it())
button_eq.grid(row=6, column=1)

button_eq = Button(text="Долары->Рубли", height=0, width=11, command=lambda: Thread(target=dollar).start()) # тут используется новый поток, чтобы не блокировать текущий.Благодаря ему, при запросе на сайт программа не виснет
button_eq.grid(row=6, column=0)

button_eq = Button(text="Евро->Рубли", height=0, width=11, command=lambda: Thread(target=eur).start()) # тут используется новый поток, чтобы не блокировать текущий.Благодаря ему, при запросе на сайт программа не виснет
button_eq.grid(row=6, column=2)

root.mainloop()