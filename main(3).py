from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
import selenium.common.exceptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading as th
import pyautogui

from audio_recorder import record_audio
from video_recorder import record_video

DRIVER_PATH = "./chromedriver.exe"
service = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)


def access_denied_error(message:str):
    if message is not None:
        pyautogui.alert(message + " and access to the directory was denied")
    else:
        pyautogui.alert("Access to the directory was denied")

def reject_cookies():
    try:
        elements = driver.find_elements(By.CSS_SELECTOR, "#dialog button.yt-spec-button-shape-next--mono")
        elements[0].click()
    except NoSuchElementException:
        print("No cookie pop up found")


def play_youtube_video():
    try:
        driver.maximize_window()
        driver.get("https://www.youtube.com/")
    except selenium.common.exceptions.WebDriverException:
        print("No internet connection")
        try:
            with open("log.txt", "w") as log:
                log.write("No internet connection")
        except PermissionError:
            access_denied_error("No internet connection")
        exit(1)
    wait = WebDriverWait(driver, 30)
    reject_cookies()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#search')))
    search_bar = driver.find_element(By.CSS_SELECTOR, 'input#search')
    search_bar.click()
    search_bar.send_keys("Skillet Victorious")

    # For some reason click operation has to be performed twice, maybe the window is out of focus because of the cookie pop up
    sleep(3)
    driver.find_element(By.ID, "search-icon-legacy").click()
    driver.find_element(By.ID, "search-icon-legacy").click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a#video-title')))
    driver.find_elements(By.CSS_SELECTOR, 'a#video-title')[0].click()

    # prevent the browser from closing for 10 seconds
    sleep(30)
    driver.quit()


# record_audio_thread = th.Thread(target=record_audio, args=[60])
# record_audio_thread.start()
play_youtube_video_thread = th.Thread(target=play_youtube_video)
play_youtube_video_thread.start()
# record_video(60)
play_youtube_video_thread.join()
# record_audio_thread.join()

