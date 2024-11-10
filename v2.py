from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inițializarea driverului cu Service
DRIVER_PATH = "./chromedriver.exe"
service = Service(DRIVER_PATH)


def create_driver():
    # Creează și returnează o nouă sesiune de browser
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


# Funcție pentru a respinge cookies
def reject_cookies(driver):
    try:
        if driver.window_handles:  # Verifică dacă fereastra este activă
            elements = driver.find_elements(By.CSS_SELECTOR, "#dialog button.yt-spec-button-shape-next--mono")
            if elements:
                elements[0].click()
            else:
                print("Butonul pentru cookies nu a fost găsit")
        else:
            print("Fereastra browserului este închisă.")
    except NoSuchElementException:
        print("Nu a fost găsit pop-up-ul de cookies")
    except NoSuchWindowException:
        print("Fereastra browserului este închisă, nu se pot respinge cookies")


# Funcția principală pentru căutare și rulare videoclip YouTube
def search_and_play_video(driver, query):
    try:
        driver.get("https://www.youtube.com/")
        wait = WebDriverWait(driver, 30)

        # Respinge pop-up-ul de cookies, dacă există
        reject_cookies(driver)


        search_bar = driver.find_element(By.CSS_SELECTOR, 'input#search')
        search_bar.click()
        search_bar.send_keys(query)

        sleep(3)

        # Execută căutarea
        search_icon = driver.find_element(By.ID, "search-icon-legacy")
        search_icon.click()
        search_icon.click()  # A doua dată pentru a preveni probleme de focalizare

        # Așteaptă și redă primul videoclip
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a#video-title')))
        driver.find_elements(By.CSS_SELECTOR, 'a#video-title')[0].click()

        # Lasă browserul deschis pentru a viziona videoclipul
        sleep(10)
    except NoSuchWindowException:
        print("Fereastra browserului s-a închis în mod neașteptat.")
        driver.quit()  # Închide sesiunea curentă, dacă mai există
        driver = create_driver()  # Crează o nouă sesiune de browser
        search_and_play_video(driver, query)  # Repornește căutarea
    except Exception as e:
       print(f"A apărut o eroare: {e}")
       driver.quit()


# Inițializare driver și rulare
driver = create_driver()
search_and_play_video(driver, "Skillet Victorious")
driver.quit()  # Închide sesiunea după execuția scriptului
