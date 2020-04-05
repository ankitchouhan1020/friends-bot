# ###########################
# F.R.I.E.N.D.S QUIZ SOLVER
# ###########################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

clear_cmd = "clear"

with open('data.json') as f:
  data = json.load(f)
  questions = data['questions']
  answers = data['answers']  

def clear():
    return os.system(clear_cmd)

def getAnswer(question):
    global questions
    global answers
    index = questions.index(question)
    return answers[index]


def solve():
    clear()
    print(r'''



                    
 d8b                                                                      d8b           d8,          
 ?88                                                                      88P          `8P           
  88b                                                                    d88                         
  888888b  d8888b  ?88   d8P  d8P    ?88   d8P  d8888b ?88   d8P     d888888   d8888b   88b  88bd88b 
  88P `?8bd8P' ?88 d88  d8P' d8P'    d88   88  d8P' ?88d88   88     d8P' ?88  d8P' ?88  88P  88P' ?8b
 d88   88P88b  d88 ?8b ,88b ,88'     ?8(  d88  88b  d88?8(  d88     88b  ,88b 88b  d88 d88  d88   88P
d88'   88b`?8888P' `?888P'888P'      `?88P'?8b `?8888P'`?88P'?8b    `?88P'`88b`?8888P'd88' d88'   88b
                                            )88                                                      
                                           ,d8P                                                      
                                        `?888P'           


                                                                             
    ''')

    driver_path = './chromedriver'
    username = input("Please enter your name: ")
    if(username == ''):
        name:'no_one'

    print('************************************************************************************')
    driver = webdriver.Chrome(executable_path = driver_path)

    driver.get('https://howyoudoin.netlify.com/')
    
    username_input = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='outlined-basic']")))
    username_input.send_keys(username)

    time.sleep(2)

    button_free = WebDriverWait(driver, 60).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[class="start-button"]')))
    button_free.click()

    while(1):
        question = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[2]")))
        question = question.get_attribute('innerHTML')
        question = question.strip()

        answer = getAnswer(question)
        answer_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='outlined-basic']")))
        answer_input.send_keys(answer)
        
        time.sleep(2)

        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, "//span[@class='MuiButton-label']")))
        submit_button.click()

        time.sleep(1)
        try:
            answer_status =WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                    (By.XPATH, "//h3[@id='answer-status']")))
            answer_status = answer_status.get_attribute('innerHTML')
            print(answer_status)

            if(answer_status == '' or answer_status == 'Correct Answer'):
                print(f'{bcolors.OKGREEN}[SUCCESS] Correct Answer.\n')
            else:
                print(f'{bcolors.WARNING}[FAILED] Wrong Answer\n')
            print('Question: ' + question)
            print('Answer: ' + answer)
        except:
            print('Hey.. done with quiz... Keep Experimenting..')
            input('Press enter to cloes the tab.')
            return

solve()
