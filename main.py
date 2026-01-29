import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)

year = 2024

dates = pd.date_range(start=f'{year}-01-01', end=f'{year}-12-31', freq='D')

data_rows = []
for date_time in dates:
    date = str(date_time)[:10]
    url = f'https://www.taladsrimuang.com/site/product/report_all.php?check_price_date={date}&id=3'
    try:
        driver.get(url)
        #print(driver.title)
        
        table = driver.find_element(By.TAG_NAME, "table")  # Replace with your table locator
        rows = table.find_elements(By.TAG_NAME, "tr")
        
        target_value = "ชมพู่ทับทิมจันทร์"  # e.g., "ID123"
        
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if cells and cells[0].text.strip() == target_value:
                # Found matching row; now interact with it (e.g., click)
                #row_data = [cell.text for cell in cells]
                price_data = cells[1].text
                if "-" in price_data:
                    lower_data, upper_data = price_data.split("-")
                    lower_value, upper_value = int(float(lower_data)), int(float(upper_data))
                else:
                    lower_value = upper_value = int(float(price_data))
                print(f'{date},{lower_value},{upper_value}')
                data_rows.append([date,lower_value,upper_value])
                break
    except Exception as e:
        pass
        #print(f'{date} has an error {e}')

#df_rows = pd.DataFrame(data_rows, #columns=['date', 'lower', 'upper'])
#df_rows.to_csv(f'{year}.csv', index=False)
driver.quit()
