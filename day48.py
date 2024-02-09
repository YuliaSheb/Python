from selenium import webdriver


chrome_driver_path = r"C:\Users\Юля\Documents\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("https://www.frontendmentor.io/challenges/space-tourism-multipage-website-gRWj1URZ3")
