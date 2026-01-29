import pandas as pd
url = 'https://www.taladsrimuang.com/site/product/report_all.php?id=3'

#read all HTML tables from specific URL
tabs = pd.read_html(url)

#display total number of tables read
print(len(tabs))