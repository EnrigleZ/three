from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import datetime
from util import output, parse_table

def fetch_weather(driver):
    url_prefix = "http://www.tianqihoubao.com/lishi/xian/month/%d%02d.html"
    
    header, rows = None, []

    for year in range(2014, 2019):
        for month in range(1, 13):
            # this is web link we are gonna fetch
            url = url_prefix%(year, month)

            driver.get(url)

            source = driver.page_source
            soup = BeautifulSoup(source, "html.parser")
            print(soup.prettify(), file=open("test.txt", "w"))

            table = soup.find("tbody")
            all_data = table.find_all("tr")
            
            table_header = all_data[0]
            all_data = all_data[1: ] 

            header, _rows = parse_table(table_header, all_data)
            rows.extend(_rows)
    
    output(header, rows, "weather.txt")
            

            


def fetch_pollution(driver):
    # this is web link we are gonna fetch.
    url = "https://www.aqistudy.cn/historydata/monthdata.php?city=%E8%A5%BF%E5%AE%89"

    # those steps below are how crawler get prepared.
    # we use variable "driver" to simulate a Chrome browser.
    driver.get(url)

    while True:
        # we need some time to get data loaded.
        time.sleep(1)

        # now all the weather data on webpage is here
        source = driver.page_source

        # we use tool "BeautifulSoup" to parse data from source page
        soup = BeautifulSoup(source, "html.parser")

        # parse data table from webpage
        table = soup.find("table")

        # get table_rows from table, each row represents a record.
        # we select row from the 2nd ([1:]), because first 
        all_data = table.find_all("tr")

        if len(all_data) > 1:
            break

    table_header = all_data[0]
    all_data = all_data[1: ]

    header, rows = parse_table(table_header, all_data)

    output(header, rows)



if __name__ == "__main__":

    driver = webdriver.Chrome()

    fetch_weather(driver)
    fetch_pollution(driver)

    print("Wait for Chrome browser window to close")
    driver.quit()