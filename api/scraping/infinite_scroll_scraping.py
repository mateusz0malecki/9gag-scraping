import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_scrolled_page_content(link):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    scroll_pause_time = 1
    screen_height = driver.execute_script("return window.screen.height;")
    i = 1

    while True:
        driver.execute_script(f"window.scrollTo(0, {screen_height * i});")
        i += 1
        time.sleep(scroll_pause_time)
        # scroll_height = driver.execute_script("return document.body.scrollHeight;")
        if i > 10:
            break

    bs = BeautifulSoup(driver.page_source, 'html.parser')
    return bs
