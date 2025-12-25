import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.Helper import highlight, textAssertion

Driver= webdriver.Chrome()
Driver.maximize_window()
Driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Logo=Driver.find_element(By.XPATH,"//img[@class='logoClass']")
highlight(Logo,Driver,0.9)
BlinkingText=Driver.find_element(By.XPATH,"//a[starts-with(text(),'Free Access ')]")
highlight(BlinkingText,Driver,0.9)
TextFromBlinkingActual=BlinkingText.text
TextFromBlinkingExpected = "Free Access to InterviewQues/ResumeAssistance/Material"
textAssertion(TextFromBlinkingActual,TextFromBlinkingExpected,Driver)
time.sleep(5)
Driver.close()