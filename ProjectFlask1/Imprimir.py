from win32print import *
import win32api
import time
import pyautogui


def print_pedido(filename):

    # with open(filename, "w", encoding="utf-8") as f:
    #    f.write(texto)
    # win32print.SetDefaultPrinter('L355 Series(Rede)')
    SetDefaultPrinter('Microsoft Print to PDF')
    # win32print.SetDefaultPrinter(r'\\bavps3001\BH_AltaVila_Printers')
    win32api.ShellExecute(
        0,
        "print",
        filename,
        '"%s"' % GetDefaultPrinter(),
        ".",
        0
    )
    # Apenas para teste
    time.sleep(1.3)
    pyautogui.typewrite("pedido")
    time.sleep(.5)
    pyautogui.press("enter")
    time.sleep(.5)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(.5)
