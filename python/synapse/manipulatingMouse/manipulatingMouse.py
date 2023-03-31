import pyautogui    # cool library
import webbrowser as browser
import time

# this is specific to my computer
browser.open('https://google.com')
time.sleep(2)
pyautogui.moveTo(2300, 10)
pyautogui.leftClick()
pyautogui.hotkey("ctrlleft", "n")
pyautogui.moveTo(3800, 10, duration=1)
pyautogui.leftClick()
pyautogui.moveTo(2300, 50, duration=1)
pyautogui.leftClick()
pyautogui.write('youtube.com')
pyautogui.press('enter')