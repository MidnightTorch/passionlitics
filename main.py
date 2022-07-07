import pyautogui
import time
import tkinter
import keyboard


tk = tkinter.Tk()


def parse_page():
    pyautogui.press('up')
    pyautogui.hotkey('fn', 'f12')
    pyautogui.hotkey('ctrl', '`')
    time.sleep(1)
    pyautogui.write('parse_card()')
    keyboard.send('enter')
    time.sleep(1)

    result = tk.clipboard_get()
    with open('result3.csv', 'a') as result_file:
        result_file.write(result.replace('\n', '') + '\n')

    time.sleep(1)
    pyautogui.hotkey('fn', 'f12')
    pyautogui.press('left')


for i in range(100):
    parse_page()

