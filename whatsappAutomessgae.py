# import pywhatkit as pyw
# pyw.sendwhatmsg('+923460864256' , 'wellcome to ansab' , 11,15)
import pyautogui as pt
import time

limit = input("Enter Limit : - ")
messsage = input("Enter Message : -")

i=0

time.sleep(2)
while i <int(limit):
    pt.typewrite(messsage)
    pt.press("enter")

    i+=1
    

