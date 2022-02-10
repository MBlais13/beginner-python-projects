# this terrible code was written by mblais

# -selenium webdriver-
from distutils.log import error
from logging import fatal
from multiprocessing.connection import wait
from sqlite3 import Time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

# getting the current local time
from datetime import date, datetime
from time import strftime
import time
# requests for sending discord webhooks
import requests

#
# welcome to my shitty code.. don't look to hard or your brain will start to hurt..
#

#Options = Options()  
#Options.add_argument("--headless")

current_time = datetime.now().date()

# -- config --
#config_student_number = '35101000'  # your student number
config_student_number = '35101896'
#config_student_dob = '2000-00-00'   # your date of birth - must be correct or you will get an error
config_student_dob = '2005-09-13'
DiscordWebhookURL = 'https://discord.com/api/webhooks/925981240358744076/Rot9AwPMNKyQAL7rxkCDDJ1l9ASkL4SQ3FuvxpZU9fvg4_uimFKHoxcVBP7lAacvhvep'    # if you do not wish to use a discord webhook use 'na'

# get the webdriver you want to use.
browser = webdriver.Firefox(executable_path=r'.\webdrivers\geckodriver.exe')
browser.get('https://covid-assessment.publicboard.ca/')
browser.implicitly_wait(10)

#wait = WebDriverWait(browser, 2)

errorcount = 0
surveysent = False
discordhooksent = False

print('This is for educational purposes only!')
print('--------------------------------------')

try: # page 1   - selection
    student_button = WebDriverWait(browser, 20).until(lambda x: x.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/fieldset/label[2]'))  # waits
    student_button.click()

    try: # page 2   - input
            # student number input
        student_number_input = WebDriverWait(browser, 5).until(lambda x: x.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/input'))  # waits
        student_number_input.send_keys(config_student_number)
            # dob input
        dob_input = WebDriverWait(browser, 5).until(lambda x: x.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/input'))  # waits
        dob_input.send_keys(config_student_dob)

        try: # page 3   - verify
            verify_button = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/input')
            verify_button = WebDriverWait(browser, 5).until(lambda x: x.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/input'))  # waits
            if verify_button.is_displayed() == True:
                verify_button.click()
            else:
                print('this means the button is not visible')

            error_message = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[4]')
            #error_message = WebDriverWait(browser, 5).until(lambda x: x.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[4]'))  # waits
            if error_message.is_displayed() == False: # if not visible
                print('error is not visible')
                try: # page 4   - confirm
                    confirm_button = WebDriverWait(browser, 5).until(lambda x: x.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/center/div/div/fieldset/label[1]'))    # waits
                    confirm_button.click()
                    
                    print('the covid assessment has been submitted.')
                    surveysent = True
                except:
                    print('failed confirm') 
                    errorcount = errorcount + 1
            else:
                print('failed; error message visible')
                errorcount = errorcount + 1
        except:
            print('failed verify')
            errorcount = errorcount + 1
    except:
        print('failed input')
        errorcount = errorcount + 1
except:
    print('failed selection')
    errorcount = errorcount + 1

print('--------------------------------------')
print(f'--- Stats ---\nCovid Survey Sent: {surveysent}\nDiscord Webhook Sent: {discordhooksent}\nError count: {errorcount}\n\n-Made with love by MBlais')










# checks if discord webhooks are disabled, if true; skips.
# if DiscordWebhookURL != 'na':
#     # sends discord webhook notification after completion.
#     discordhooksent = True
#     embed = {
#         "title": "Covid Assessment Bot",
#         "color": (15052624 if errorcount >= 1 else 5546086), # dark green:5546086, light green:8776060
#         "fields": [
#             {
#             "name": ('ERRORS!' if errorcount >= 1 else 'Code ran smoothly.'),
#             "value": (f'--- Stats ---\nCovid Survey Sent: {surveysent}\nDiscord Webhook Sent: {discordhooksent}\nError count: {errorcount}')
#             }
#         ],
#         "footer": {
#             "text": (f"Made by MBlais.dev • {current_time} , • CovidBot"),
#             "icon_url": "https://i.imgur.com/MbrG9HM.png"
#         }
        
#         }

#     data = {
#         "username": "Covid Assessment Bot",
#         "avatar_url": "https://i.imgur.com/eVDSFTr.png",
#         "embeds": [
#             embed
#             ],
#     }

#     headers = {
#         "Content-Type": "application/json"
#     }

#     result = requests.post(DiscordWebhookURL, json=data, headers=headers)
#     if 200 <= result.status_code < 300:
#         print(f"Webhook sent {result.status_code}")
#     else:
#         print(f"Not sent with {result.status_code}, response:\n{result.json()}")
