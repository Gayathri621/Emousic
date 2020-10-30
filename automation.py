from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

emotion = input("Enter your emotion(in lowercase)") 

if emotion == "happy":
    wrds = ["The cure- Friday i'm in love", "The Beatles i want to hold your hand", "Beautiful day"]
    kwrd = ["Cure", "Beatles", "Beautiful"]
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    driver=webdriver.Chrome(chrome_options=options, executable_path=r'/home/akshat/chromedriver')#add the path for the chromedriver
    for i, j in zip(wrds, kwrd):
        driver.get("https://www.youtube.com/")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(i)
        driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3.title-and-badge.style-scope.ytd-video-renderer a"))).click()
        WebDriverWait(driver, 10).until(EC.title_contains(j))
        print(driver.current_url)
        
        
elif emotion == "angry":
    wrds = ["Maroon 5 - Memories", "The Weeknd - Blinding Lights", "Lloyd P White - Burst Part 2"]
    kwrd = ["maroon", "weeknd", "lloyd"]
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    driver=webdriver.Chrome(chrome_options=options, executable_path=r'/home/akshat/chromedriver')
    for i, j in zip(wrds, kwrd):
        driver.get("https://www.youtube.com/")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(i)
        driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3.title-and-badge.style-scope.ytd-video-renderer a"))).click()
        WebDriverWait(driver, 10).until(EC.title_contains(j))
        print(driver.current_url)
        
elif emotion == "sad":
    wrds = ["I'll Meet You There - Sapajou", "Relax - Markvard", "Wake Up (feat. ROMY DYA) - Wataboi"]
    kwrd = ["I'll Meet You There", "Relax", "Wake Up"]
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    driver=webdriver.Chrome(chrome_options=options, executable_path=r'/home/akshat/chromedriver')
    for i, j in zip(wrds, kwrd):
        driver.get("https://www.youtube.com/")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(i)
        driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3.title-and-badge.style-scope.ytd-video-renderer a"))).click()
        WebDriverWait(driver, 10).until(EC.title_contains(j))
        print(driver.current_url)
        
elif emotion == "neutral":
    wrds = ["Becky Hill - Space", "Justin Bieber & benny blanco - Lonely", "Little Mix - Happiness"]
    kwrd = ["Becky Hill", "Justin Bieber & benny blanco", "Little Mix"]
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    driver=webdriver.Chrome(chrome_options=options, executable_path=r'/home/akshat/chromedriver')
    for i, j in zip(wrds, kwrd):
        driver.get("https://www.youtube.com/")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(i)
        driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3.title-and-badge.style-scope.ytd-video-renderer a"))).click()
        WebDriverWait(driver, 10).until(EC.title_contains(j))
        print(driver.current_url)        
        
driver.quit()        
