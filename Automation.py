import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.Helper import highlight
Driver= webdriver.Chrome()
Driver.maximize_window()
Driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Logo=Driver.find_element(By.XPATH,"//img[@class='logoClass']")
highlight(Logo,Driver,0.9)
BlinkingText=Driver.find_element(By.XPATH,"//a[starts-with(text(),'Free Access ')]")
highlight(BlinkingText,Driver,0.9)
TextFromBlinking=BlinkingText.text
try:
    assert TextFromBlinking=="Free Access to InterviewQues/ResumeAssistance/Material", "Opps! didn't found."
except Exception as e:
    print(e)
time.sleep(5)
Driver.close()