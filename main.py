from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
# from datetime import datetime
import time


options = Options()
options.add_argument("--headless")
# driver = webdriver.Firefox(options=options)
# driver.get("https://google.com")
# print(driver.title)

# chrome_options = Options()
# options = [
#     "--headless",
#     "--disable-gpu",
#     "--window-size=1920,1200",
#     "--ignore-certificate-errors",
#     "--disable-extensions",
#     "--no-sandbox",
#     "--disable-dev-shm-usage"
# ]
# for option in options:
#     chrome_options.add_argument(option)

def app_test():
    url = 'https://www.thaiupdate.info/rising-female-star-2024-group-3/'

    driver = webdriver.Firefox(options=options)
    driver.get(url)
    print(driver.title)
    for _ in range(60): # ran 60 round 
        try:
            for _ in range(5):
                # vote for yada
                yada_select = driver.find_element(By.ID, "PDI_answer61165598")
                driver.execute_script("arguments[0].click();", yada_select)
                driver.implicitly_wait(1)

                vote_button = driver.find_element(By.ID, "pd-vote-button13699609")
                driver.execute_script("arguments[0].click();", vote_button)
                driver.implicitly_wait(5)

                ## captcha Ex. 9 + 10 =
                captcha = driver.find_element(By.CSS_SELECTOR, ".h-captcha > span > p")
                # print(captcha.text)
                cap_text = captcha.text
                cap_list = cap_text.split() # Ex. ["9", "+", "10", "="]
                cap_answer = int(cap_list[0])+int(cap_list[2])
                # print(cap_answer)
                driver.find_element(By.NAME, "answer").send_keys(cap_answer)
                driver.implicitly_wait(1)

                final_vote_button = driver.find_element(By.CSS_SELECTOR, ".pds-vote-button")
                driver.execute_script("arguments[0].click();", final_vote_button)

                driver.implicitly_wait(5)

                # return pull 
                return_button = driver.find_element(By.CSS_SELECTOR, ".pds-return-poll")
                driver.execute_script("arguments[0].click();", return_button)
        except: 
            print("has error")
        finally:
            time.sleep(90) # wait 90 seconds before start again
        
    driver.quit()

if __name__ == '__main__':
    # start_time = datetime.now()
    # print('Time start:', str(start_time))
    app_test()
    # end_time = datetime.now()
    # print('Time end:', str(end_time))
    # print('Time difference:', str(end_time - start_time))
