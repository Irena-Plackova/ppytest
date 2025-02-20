from selenium import webdriver
import time

# Spuštění WebDriveru
driver = webdriver.Chrome()

# Otevře intranetovou stránku
driver.get("https://intranet.dpo.cz/kontakty/")

# Počkej na načtení
time.sleep(3)

# Získá celé HTML stránky
html_source = driver.page_source

# Uloží do souboru pro snadnější analýzu
with open("intranet_dpo_kontakty.html", "w", encoding="utf-8") as file:
    file.write(html_source)

print("✅ HTML kód stránky uložen do souboru intranet_dpo_kontakty.html.")

# Zavře prohlížeč
driver.quit()
