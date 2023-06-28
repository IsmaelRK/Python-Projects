import pyautogui


write_var = 0

pyautogui.typewrite(f"", interval=2000)

while write_var < 100:
    pyautogui.typewrite(f"{write_var}", interval=0)
    pyautogui.press('enter')
    write_var += 1
