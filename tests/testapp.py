import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

parser = argparse.ArgumentParser(description='Testing code for weather app')
parser.add_argument('--zip', type=str, help='Zip code', required=True)
parser.add_argument('--location', type=str, help='A city Name for the given Zip code', required=True)
parser.add_argument('--app_address', type=str, help='Address of the WeatherApp', required=True)

args = parser.parse_args()
zip_code = args.zip
location = args.location
app_address = args.app_address

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920x1080")
options.add_argument("--remote-debugging-port=9222")

service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

def wait_for_element(kind, name):
    if kind == "class":
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, name))
        )
    elif kind == "link_text":
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, name))
        )
    elif kind == "id":
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, name))
        )

def test(zip_code, location, app_address):
    try:
        driver.get(app_address)
    except Exception as e:
        return f"Failed to access {app_address} due to {e}"

    wait_for_element("id", "name")
    try:
        input_element = driver.find_element(By.ID, "name")
        input_element.send_keys(zip_code + Keys.RETURN)
    except Exception as e:
        return f"Failed to send keys to input element due to {e}"

    time.sleep(12)
    try:
        location_element = driver.find_element(By.ID, "Location")
        city = location_element.text.split('Location: ')[1].split(', ')[0]
    except Exception as e:
        return f"Failed to get location element due to {e}"

    try:
        driver.quit()
    except Exception as e:
        return f"Failed to close the browser due to {e}"

    return "Test passed" if city == location else "Test failed"

result = test(zip_code, location, app_address)

print(result)
