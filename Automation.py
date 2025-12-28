import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.driver_finder import DriverFinder
from selenium.webdriver.support.select import Select

from utils.Helper import highlight, textAssertion, clickFunction, selectOptions, prompt

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

tab1=Driver.find_element(By.CSS_SELECTOR,"div[id='radio-btn-example'] fieldset legend")
highlight(tab1,Driver,0.9)

radieo1=Driver.find_element(By.XPATH,"//label[normalize-space()='Radio1']/child::input")
clickFunction(radieo1,Driver)
radieo2=Driver.find_element(By.XPATH,"//label[normalize-space()='Radio2']/child::input")
clickFunction(radieo2,Driver)
radieo3=Driver.find_element(By.XPATH,"//label[normalize-space()='Radio3']/child::input")
clickFunction(radieo3,Driver)

tab2=Driver.find_element(By.XPATH,"//legend[normalize-space()='Suggession Class Example']")
highlight(tab2,Driver,0.9)
input1=Driver.find_element(By.XPATH,"//input[@id='autocomplete']")
userInput=prompt(Driver)
input1.clear()
input1.send_keys(userInput)
time.sleep(3)
selects=Driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']")
for selction in selects:
    if selction.text.lower()==userInput.lower():
        highlight(selction,Driver,0.9)
        selction.click()
        break

#Dropdowns
dropDownExample=Driver.find_element(By.XPATH,"//legend[contains(normalize-space(),'Dropdown Example')]")
highlight(dropDownExample,Driver,0.9)
inpus=Driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']")
selectOptions(inpus)
# rahul=Driver.find_element(By.XPATH,"//a[contains(text(),'RAHUL')]")
# highlight(rahul,Driver,0.9)

checkBox=Driver.find_element(By.CSS_SELECTOR,"div[id='checkbox-example'] legend")
highlight(checkBox,Driver)


time.sleep(5)
Driver.close()