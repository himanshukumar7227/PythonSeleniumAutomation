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

# Check Box :
checkBox=Driver.find_element(By.CSS_SELECTOR,"div[id='checkbox-example'] legend")
highlight(checkBox,Driver)
for i in range(1,4):
    m=Driver.find_element(By.XPATH,"//label[normalize-space()='Option"+str(i)+"']")
    highlight(m,Driver,0.9)
    n=Driver.find_element(By.XPATH,"//label[normalize-space()='Option"+str(i)+"']/child::input")
    n.click()

# New window opening and closing automation
swichExample=Driver.find_element(By.XPATH,"//legend[normalize-space()='Switch Window Example']")
highlight(swichExample,Driver,0.9)
openWindowBtn=Driver.find_element(By.CSS_SELECTOR,"#openwindow")
highlight(openWindowBtn,Driver,0.9)
openWindowBtn.click()
windowsOpen=Driver.window_handles
Driver.switch_to.window(windowsOpen[1])
Driver.maximize_window()
loggo=Driver.find_element(By.XPATH,"(//img[@alt='Logo'])[1]")
highlight(loggo,Driver,0.9)
Driver.close()
Driver.switch_to.window(windowsOpen[0])

# New Tab
switchTab=Driver.find_element(By.XPATH,"//legend[@class='switch-tab']")
highlight(switchTab,Driver,0.9)
switchTabclk=Driver.find_element(By.XPATH,"//a[@id='opentab']")
switchTabclk.click()
windowsOpen=Driver.window_handles
Driver.switch_to.window(windowsOpen[1])
loggo=Driver.find_element(By.XPATH,"(//img[@alt='Logo'])[1]")
highlight(loggo,Driver,0.9)
Driver.close()
Driver.switch_to.window(windowsOpen[0])
highlight(Logo,Driver,0.9)

# Alert And Promt
alertt=Driver.find_element(By.XPATH,"//legend[normalize-space()='Switch To Alert Example']")
highlight(alertt,Driver,0.9)
alerBtntxt=prompt(Driver)
alertBtn=Driver.find_element(By.CSS_SELECTOR,"#name")
alertBtn.send_keys(alerBtntxt)
clkalert=Driver.find_element(By.CSS_SELECTOR,"#alertbtn")
clkalert.click()
windowsOpen=Driver.window_handles
al=Driver.switch_to.alert
print(al.text)
time.sleep(2)
al.accept()




time.sleep(3)
Driver.close()