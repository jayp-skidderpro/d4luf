import requests
import string
from time import sleep
from random import randint

sleep(0.25)
print('\nd4luf (discord 4 letter username finder')
sleep(0.5)
token = str(input('input discord authorization token (must be exact): '))
delay = float(input('\ninput delay (how many seconds in-between each username attempt, lower values may result in faster rate limiting): '))
username = ''

pos = list(string.ascii_lowercase)
pos.extend(list(string.digits))

def pomelo_attempt(username):

    headers = {
    'Content-Type':'application/json',
    'Authorization':token
    }
    payload = {
    'username':username
    }
    response = requests.post('https://discord.com/api/v9/users/@me/pomelo-attempt', headers=headers, json=payload)
    
    return response

print('\nUSING D4LUF (DISCORD 4 LETTER USER FINDER) IS AGAINST DISCORD TOS AND MAY RESULT IN ACTION BEING TAKEN ON YOUR ACCOUNT, I HAVE LITERALLY 0 CLUE WHAT IM DOING MAKING THIS, USE D4LUF AT YOUR OWN RISK!!!')
sleep(1)
print('YOU MAY BE RATE LIMITED VERY FAST, USING A LARGER DELAY FOR MORE TIME')
sleep(1)
print('I WOULD SUGGEST MAKING AN ALT AND USE THAT TOKEN INSTEAD TO MITIGATE ACCOUNT RISK')
sleep(1.25)
print(f'\nBEGINNING INDEFINITE SCAN USING TOKEN >{token}< >1 user per {delay} sec.<\n\n')
sleep(0.25)
    
while True:
    username = []
    i = 0
    while i <= 3:
        username.append(pos[randint(0, (len(pos)-1))])
        i += 1
    username = ''.join(username)
    print(f'd4luf attempting username: {username}')
    print(pomelo_attempt(username).text)
    print('\n')
    sleep(delay)
