import pyautogui
import time

pyautogui.PAUSE = 0.3

# Define o número de repetições desejado
repeticoes = 5

for _ in range(repeticoes):
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.click(x=587, y=300)
    time.sleep(3)
    pyautogui.click(x=674, y=629)
    time.sleep(3)
    pyautogui.click(x=1165, y=18)
    pyautogui.write("www.youtube.com.br")
    pyautogui.press("enter")
    pyautogui.click(x=630, y=148)
    time.sleep(3)
    pyautogui.write("Grau Técnico")
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.click(x=548, y=591)
   

    time.sleep(5)
