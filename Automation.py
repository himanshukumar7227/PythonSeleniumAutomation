import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.driver_finder import DriverFinder

from utils.Helper import highlight, textAssertion, clickFunction

Driver= webdriver.Chrome()
Driver.implicitly_wait(10)
Driver.maximize_window()
Driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Logo=Driver.find_element(By.XPATH,"//img[@class='logoClass']")
highlight(Logo,Driver,0.9)
BlinkingText=Driver.find_element(By.XPATH,"//a[starts-with(text(),'Free Access ')]")
highlight(BlinkingText,Driver,0.9)
TextFromBlinkingActual=BlinkingText.text
TextFromBlinkingExpected = "Free Access to InterviewQues/ResumeAssistance/Material"
textAssertion(TextFromBlinkingActual,TextFromBlinkingExpected,Driver)
homeButton=Driver.find_element(By.XPATH,"//button[contains(text(),'Home')]")
highlight(homeButton,Driver,0.9)
praticeButton=Driver.find_element(By.XPATH,"//button[normalize-space()='Practice']")
highlight(praticeButton,Driver,0.9)
loginButton=Driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
highlight(loginButton,Driver,0.9)
signupButton=Driver.find_element(By.XPATH,"//button[normalize-space()='Signup']")
highlight(signupButton,Driver,0.9)
PracticeTitle=Driver.find_element(By.TAG_NAME,'h1')
highlight(PracticeTitle,Driver,0.9)
radieo1=Driver.find_element(By.XPATH,"//label[normalize-space()='Radio1']/child::input")
clickFunction(radieo1,Driver)
radieo2=Driver.find_element(By.XPATH,"//label[normalize-space()='Radio2']/child::input")
clickFunction(radieo2,Driver)
radieo3=Driver.find_element(By.XPATH,"//label[normalize-space()='Radio3']/child::input")
clickFunction(radieo3,Driver)
tab1=Driver.find_element(By.CSS_SELECTOR,"div[id='radio-btn-example'] fieldset legend")
highlight(tab1,Driver,0.9)

# rahul=Driver.find_element(By.XPATH,"//a[contains(text(),'RAHUL')]")
# highlight(rahul,Driver,0.9)

time.sleep(5)
Driver.close()