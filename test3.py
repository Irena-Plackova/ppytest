import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    """Inicializuje webdriver pro Chrome"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_automaticke_doplnovani(driver):
    """Ověří automatické doplňování při vyhledávání kontaktů"""
    driver.get("https://intranet.dpo.cz/kontakty/")

    WebDriverWait(driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")

    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "vstup-vyhledavani")))
    search_box.send_keys("Jan")  # Zadáme první tři písmena

    time.sleep(2)

    suggestions = driver.find_elements(By.CSS_SELECTOR, ".suggestion-class")  # Ověř z webu skutečný CSS selektor
    assert len(suggestions) > 0, "❌ Automatické doplňování nefunguje"

    print("✅ Automatické doplňování funguje správně")


def test_vyhledavani_kontaktu(driver):
    """Ověří funkčnost tlačítka hledání"""
    driver.get("https://intranet.dpo.cz/kontakty/")

    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "vstup-vyhledavani")))
    search_box.send_keys("Jan Novák")

    search_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")  # Selektor tlačítka "Hledat"
    search_button.click()

    time.sleep(3)

    assert "Jan Novák" in driver.page_source, "❌ Kontakt nebyl nalezen"
    print("✅ Kontakt byl nalezen správně")


def test_negativni_vyhledavani(driver):
    """Ověří vyhledávání neexistujícího kontaktu"""
    driver.get("https://intranet.dpo.cz/kontakty/")


    time.sleep(3)

