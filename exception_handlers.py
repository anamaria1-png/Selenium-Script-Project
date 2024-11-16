import pyautogui


def access_denied_error(message:str):
    if message is not None:
        pyautogui.alert(message + " and access to the directory was denied")
    else:
        pyautogui.alert("Access to the directory was denied")


def show_error(message: str):
    pyautogui.alert(message)