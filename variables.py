from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Spuštění prohlížeče
driver = webdriver.Chrome()
driver.get("https://intranet.dpo.cz/kontakty/")

try:
    # Počkáme, než se objeví tlačítko pro SSO přihlášení (max 10 sekund)
    wait = WebDriverWait(driver, 10)
    sso_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Přihlásit pomocí SSO")))

    # Kliknutí na tlačítko
    sso_button.click()
    time.sleep(3)

    # Ověření přesměrování na SSO login stránku
    assert "sso.dpo.cz" in driver.current_url

    print("Test úspěšný: Přihlášení přes SSO bylo nalezeno a kliknuto.")

except Exception as e:
    print(f"Test selhal: {e}")

# Ukončení testu
driver.quit()
