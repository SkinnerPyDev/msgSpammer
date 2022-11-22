import pyautogui as py
import time

msg = input("Enter your message: ")
number_of_times = input("How many times you want to send: ")

time.sleep(5)

for i in range(int(number_of_times)):
    py.typewrite(msg)
    py.press("Enter")
