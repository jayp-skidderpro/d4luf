import requests
import json
from random import randint, uniform, choice
from string import ascii_lowercase, digits
from time import sleep

with open('program/user_agents.json', 'r') as file:
    uas = json.load(file)

with open('config/tokens.json', 'r') as file:
    tokens = json.load(file)

def gru(l):
    chars = ascii_lowercase + digits
    string = ''

    for i in range(0, l):
        string += chars[randint(0, len(chars) - 1)]

    return string

h = {
    'Authorization': '',
    'Content-Type': 'application/json',
    'Origin': 'https://discord.com',
    'Referer': 'https://discord.com/channels/@me',
    'User-Agent': ''
}

p = {
    'username': ''
}

while True:
    for t in tokens:
        att_u = gru(4)

        p['username'] = att_u

        h['User-Agent'] = choice(uas)

        h['Authorization'] = t

        print(f'username: {att_u}')
        r = requests.post('https://discord.com/api/v9/users/@me/pomelo-attempt', json=p, headers=h)
        print(f'{r.status_code} || {r.text}')

        with open('ulogs/ulogs.txt', 'a') as file:
            file.write(f'username: {att_u} / status_code: {r.status_code} / response: {r.text} / token used: {t}\n')

        sleep(uniform(1.5, 2.5))
