d4luf
open source discord 4 letter username finder

d4luf may be against discord tos, i do not encourage you to use d4luf for automating username searches. do not use d4luf in any way that goes against discord tos at all. i am not liable for any actions or consequences that are taken upon you by discord or similar entities. use this tool at your own risk and discretion, you have been warned. use d4luf for educational purposes only.

DO NOT CHANGE THE FILE STRUCTURE OF D4LUF IN ANY WAY! IT WILL PROBABLY BREAK!!!

INSTRUCTIONS:
-----
d4luf uses token cycling to avoid rate limiting alongside user agent cycling. it is suggested to use 3 tokens minimum to avoid rate limiting.
go into d4luf/config/tokens.json and add your token(s) to your account as a string in json format, like how the example strings are laid out.

after that, run d4luf.py to begin searching for 4 letter usernames using the token(s) you provided as authorization. do not use your main accounts token please.

if d4luf replies with taken: false, that means that username is open. you can copy or remember it and use it as you'd like, as it is available.

logs to all username captures are stored in d4luf/ulogs in a .txt file named ulogs.txt. you can open it and it will show you all usernames it has scanned, available or unavailable. this is good in-case you want to leave d4luf running without supervision so it will save the usernames and you can either look through the logs or make a scraper to search for taken: false usernames.

anyways good luck, this is not a very high quality project i made it when i was bored in a few hours lol.
-----

it repeatedly uses post requests to check if 4 letter discord usernames are open. it uses usernames randomly made up of letters a-z and numbers 0-9. it does this every 1.5-2.5 seconds.

it uses user agent cycling and token cycling to avoid rate limiting. do not use your main accounts token or any accounts you care about.

d4luf may be against discord tos, i do not encourage you to use d4luf for automating username searches. do not use d4luf in any way that goes against discord tos at all. i am not liable for any actions or consequences that are taken upon you by discord or similar entities. use this tool at your own risk and discretion, you have been warned. use d4luf for educational purposes only.ding README.md…]()

DO NOT CHANGE THE FILE STRUCTURE OF D4LUF IN ANY WAY! IT WILL PROBABLY BREAK!!!
