from time import sleep  # Importă funcția sleep pentru a adăuga pauze în execuția scriptului
from selenium import webdriver  # Importă webdriver din Selenium pentru a controla browserul
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException  # Excepții pentru elemente sau ferestre inexistente
from selenium.webdriver import Keys  # Importă Keys pentru a simula apăsările de taste
from selenium.webdriver.chrome.service import Service  # Importă Service pentru a seta serviciul ChromeDriver
from selenium.webdriver.common.by import By  # Importă By pentru localizarea elementelor pe pagină
from selenium.webdriver.support.wait import WebDriverWait  # Importă WebDriverWait pentru așteptări explicite
from selenium.webdriver.support import expected_conditions as EC  # Importă expected_conditions pentru condiții de așteptare

# Definește calea către executabilul ChromeDriver
DRIVER_PATH = "./chromedriver.exe"
service = Service(DRIVER_PATH)  # Creează un serviciu ChromeDriver cu calea specificată


def create_driver():
    """
    Creează și returnează o nouă sesiune de browser Chrome.
    """
    driver = webdriver.Chrome(service=service)  # Inițializează un obiect ChromeDriver
    driver.implicitly_wait(10)  # Setează o așteptare implicită de 10 secunde pentru elemente
    driver.maximize_window()  # Maximizează fereastra browserului
    return driver  # Returnează driverul creat


# Funcție pentru respingerea pop-up-ului de cookies, dacă există
def reject_cookies(driver):
    try:
        if driver.window_handles:  # Verifică dacă există ferestre deschise
            elements = driver.find_elements(By.CSS_SELECTOR, "#dialog button.yt-spec-button-shape-next--mono")  
            # Găsește butonul pentru respingerea cookies folosind CSS selector
            if elements:
                elements[0].click()  # Apasă pe primul buton găsit pentru respingerea cookies
            else:
                print("Butonul pentru cookies nu a fost găsit")  # Mesaj dacă butonul nu este găsit
        else:
            print("Fereastra browserului este închisă.")
    except NoSuchElementException:
        print("Nu a fost găsit pop-up-ul de cookies")  # Mesaj dacă elementul nu a fost găsit
    except NoSuchWindowException:
        print("Fereastra browserului este închisă, nu se pot respinge cookies")  # Mesaj dacă fereastra este închisă


# Funcția principală pentru căutarea și rularea unui videoclip YouTube
def search_and_play_video(driver, query):
    """
    Deschide YouTube, caută videoclipul specificat și redă primul rezultat.
    """
    try:
        driver.get("https://www.youtube.com/")  # Deschide pagina YouTube
        wait = WebDriverWait(driver, 30)  # Creează o așteptare de până la 30 secunde pentru anumite condiții

        # Respinge cookies dacă apare pop-up-ul
        reject_cookies(driver)

        # Găsește bara de căutare, dă click și introduce textul de căutare
        search_bar = driver.find_element(By.CSS_SELECTOR, 'input#search')  # Găsește bara de căutare
        search_bar.click()  # Dă click pentru a activa bara de căutare
        search_bar.send_keys(query)  # Introduce termenul de căutare specificat

        sleep(3)  # Așteaptă 3 secunde pentru stabilizarea interfeței

        # Execută căutarea prin dublu click pe butonul de căutare, în caz de probleme de focalizare
        search_icon = driver.find_element(By.ID, "search-icon-legacy")  # Găsește butonul de căutare
        search_icon.click()
        search_icon.click()  # Click dublu pentru a preveni erori de focalizare

        # Așteaptă și redă primul videoclip
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a#video-title')))  # Așteaptă până când primul rezultat devine clicabil
        driver.find_elements(By.CSS_SELECTOR, 'a#video-title')[0].click()  # Dă click pe primul videoclip din rezultate

        # Lasă browserul deschis pentru a permite vizionarea videoclipului
        sleep(10)  # Așteaptă 10 secunde pentru vizionare
    except NoSuchWindowException:
        print("Fereastra browserului s-a închis în mod neașteptat.")  # Mesaj de eroare dacă fereastra este închisă
        driver.quit()  # Închide sesiunea curentă
        driver = create_driver()  # Creează o nouă sesiune de browser
        search_and_play_video(driver, query)  # Repornește căutarea videoclipului


# Inițializare driver și rulare funcția de căutare și redare videoclip
driver = create_driver()  # Creează o instanță nouă a driverului
search_and_play_video(driver, "Skillet Victorious")  # Caută și redă videoclipul "Skillet Victorious"
driver.quit()  # Închide sesiunea de browser după execuția scriptului
