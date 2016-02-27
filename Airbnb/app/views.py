"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def home(request):
    assert isinstance(request, HttpRequest)
    return render(request,
        'app/Airbnbchangepassword.html',
        context_instance = RequestContext(request,
        {
            'title':'Airbnb Change password ',
            'year':datetime.now().year,
        }))

def Airbnbchangepassword(request):
    if request.method == 'POST':
        stremail = request.POST.get("email")
        strcurrentpassword = request.POST.get("currentpassword")
        strnewpassword = request.POST.get("newpassword")
        strconfirmpassword = request.POST.get("confirmpassword")
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get("https://www.airbnb.co.in/login")

        #Check if Email textbox is exist
        flagsignin_email=1
        while (flagsignin_email):
            try:
                flagsignin_emailelement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "signin_email")))
                flagsignin_email = 0
            except Exception as inst:
                flagsignin_email=1

        signin_email = driver.find_element_by_id('signin_email')
        signin_password = driver.find_element_by_id('signin_password')
        user_login_btn = driver.find_element_by_id('user-login-btn')

        signin_email.clear()
        signin_password.clear()
        signin_email.send_keys(stremail)
        signin_password.send_keys(strcurrentpassword)
        user_login_btn.click()

        flagaccountTab = 1
        while (flagaccountTab):
            try:
                accountelement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href,\'account\')]")))
                flagaccountTab = 0
            except Exception as inst:
                flagaccountTab = 1

        

        driver.get("https://www.airbnb.co.in/users/notifications")

        #Check if Security tab is exist
        flagsecurityTab = 1
        while (flagsecurityTab):
            try:
                securityelement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href,\'security\')]")))
                flagsecurityTab = 0
            except Exception as inst:
                flagsecurityTab = 1

        securityTab = driver.find_element_by_xpath('//a[contains(@href,\'security\')]')
        securityTab.click()

        #Check if Update Password checkbox is exist
        flagoldpassword = 1
        while (flagoldpassword):
            try:
                flagoldpasswordelement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "old_password")))
                flagoldpassword = 0
            except Exception as inst:
                flagoldpassword = 1

        old_password = driver.find_element_by_id('old_password')
        new_password = driver.find_element_by_id('new_password')
        user_password_confirmation = driver.find_element_by_id('user_password_confirmation')
        old_password.clear()
        new_password.clear()
        user_password_confirmation.clear()
        old_password.send_keys(strcurrentpassword)
        new_password.send_keys(strnewpassword)
        user_password_confirmation.send_keys(strconfirmpassword)
        user_password_confirmation.submit()
        
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class=\'flash-container\']/div")))
            user_password_confirmation = driver.find_element_by_xpath('//div[@class=\'flash-container\']/div')
            strMessage = user_password_confirmation.text()
            driver.quit()  
            return render(request,
            'app/Airbnbchangepassword.html',
            context_instance = RequestContext(request,
            {
            'title':'Airbnb Change password ',
            'Message':strMessage,
            }))
        except Exception as inst:
            driver.quit()  
            return render(request,
            'app/Airbnbchangepassword.html',
            context_instance = RequestContext(request,
            {
            'title':'Airbnb Change password ',
            'Message':inst,
            })) 
           
    elif request.method == 'GET':      
        assert isinstance(request, HttpRequest)
        return render(request,
        'app/Airbnbchangepassword.html',
        context_instance = RequestContext(request,
        {
            'title':'Airbnb Change password ',
            'year':datetime.now().year,
            
        }))





