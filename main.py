from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--headless")

def app():
    url = 'https://www.thaiupdate.info/drama-series-2024-group-1/'

    driver = webdriver.Firefox(options=options)
    driver.get(url)
    print(driver.title)
    for _ in range(60): # ran 60 round 
        try:
            for _ in range(5):
                yada_select = driver.find_element(By.ID, "PDI_answer61654935")
                driver.execute_script("arguments[0].click();", yada_select)
                driver.implicitly_wait(1)

                vote_button = driver.find_element(By.ID, "pd-vote-button13821191")
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
    app()
