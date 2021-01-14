import pyautogui

f = open("input.txt", "r")

msg = f.read()
n = 1
for i in range(0,int(n)):
  pyautogui.typewrite(msg + '\n')
  pyautogui.press("enter")
