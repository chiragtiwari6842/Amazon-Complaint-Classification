import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from classify import classify_into_categories
from check_labels import check_complaint_labels
from reply import generate_reply

def main():
    chrome_options = Options()

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://x.com/i/flow/login")
    time.sleep(3)
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "text"))
    )  

    username_field.send_keys("del_complaint")

    next_button = driver.find_element(By.XPATH, "//span[text()='Next']")  
    next_button.click()

    time.sleep(2)
    try:
        input_field = driver.find_element(By.XPATH, "//span[text()='Phone or email']/ancestor::div//input")
        input_field.send_keys("21ag1a66d9@gmail.com")
        time.sleep(4)
        next_button = driver.find_element(By.XPATH, "//span[text()='Next']")  
        next_button.click()
    except Exception:
        pass
    time.sleep(2)
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("delivery@1234")

    next_button = driver.find_element(By.XPATH, "//span[text()='Log in']")  
    next_button.click()    
    time.sleep(4)
    driver.get("https://x.com/notifications/mentions")
    time.sleep(3)
    try:
        first_tweet = driver.find_element(By.XPATH, "(//div[@data-testid='tweetText'])[1]")
        complaint_text = first_tweet.text   
    except Exception as e:
        print(f"Error extracting tweet text: {e}")
        return None
    
    complaint = complaint_text
    actual_labels = classify_into_categories(complaint)

    result, updated_labels = check_complaint_labels(complaint, actual_labels)
    if result == "No":
        labels = updated_labels
    elif result == "Yes":
        labels = actual_labels
    reply = generate_reply(complaint, labels)

    time.sleep(3)
    username = first_tweet.find_element(By.XPATH, ".//ancestor::article//span[contains(text(), '@')]").text

    reply_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='reply']"))
    )
    reply_button.click()  
    
    time.sleep(5)
    
    driver.switch_to.active_element.send_keys(username+" " + reply)
    time.sleep(10)
    post_button = driver.find_element(By.XPATH, "//button[@data-testid='tweetButton']")
    post_button.click()
    time.sleep(2)

if __name__ == '__main__':
    main()