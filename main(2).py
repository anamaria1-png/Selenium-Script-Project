from time import sleep  # Importă funcția sleep din modulul time, pentru a adăuga pauze în execuția scriptului.

from selenium import webdriver  # Importă webdriver-ul din Selenium pentru a controla browserul Chrome.
from selenium.webdriver.chrome.service import Service  # Importă Service pentru a seta serviciul ChromeDriver.
from selenium.webdriver.common.by import By  # Importă By pentru a localiza elementele în diferite moduri (ex. ID, CSS).
from selenium.webdriver.support.wait import WebDriverWait  # Importă WebDriverWait pentru a configura așteptări explicite.
from selenium.webdriver.support import expected_conditions as EC  # Importă expected_conditions (EC) pentru condiții de așteptare.

DRIVER_PATH = "./chromedriver.exe"  # Definește calea către executabilul ChromeDriver necesar pentru a automatiza Chrome.

service = Service(DRIVER_PATH)  # Creează un serviciu ChromeDriver folosind calea specificată.
driver = webdriver.Chrome(service=service)  # Inițializează o instanță Chrome a driverului, pentru a controla Chrome.

driver.implicitly_wait(10)  # Setează o așteptare implicită de 10 secunde pentru a găsi elementele înainte de a da eroare.

driver.maximize_window()  # Maximiează fereastra browserului pentru o vizualizare completă.
driver.get("https://www.youtube.com/")  # Deschide URL-ul YouTube în browserul controlat de Selenium.

wait = WebDriverWait(driver, 30)  # Definește o așteptare explicită de până la 30 de secunde pentru anumite condiții.

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#search')))  
# Așteaptă până când elementul cu selectorul CSS 'input#search' (bara de căutare YouTube) devine vizibil.

search_bar = driver.find_element(By.CSS_SELECTOR, 'input#search')  # Găsește bara de căutare pe YouTube folosind selectorul CSS.
search_bar.click()  # Dă click pe bara de căutare pentru a o activa.
search_bar.send_keys("Skillet Victorious")  # Introduce textul "Skillet Victorious" în bara de căutare.

driver.find_element(By.ID, "search-icon-legacy").click()  # Găsește și dă click pe butonul de căutare folosind ID-ul 'search-icon-legacy'.
sleep(3)  # Așteaptă 3 secunde pentru a permite YouTube-ului să încarce rezultatele căutării.

driver.find_elements(By.CSS_SELECTOR, 'a#video-title')[0].click()  # Selectează primul video din rezultate și dă click pe el.
sleep(10)  # Așteaptă 10 secunde pentru ca video-ul să înceapă să ruleze.
