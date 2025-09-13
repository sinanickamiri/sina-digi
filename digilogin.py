# import packages
import requests, urllib3, json, pyfiglet

# disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# make the program more modern
text = "K o o r i  D i g i l o g g e r"

ascii_banner = pyfiglet.figlet_format(text, width=200)
print(ascii_banner)

# creating session
r = requests.session()

# settting proxies for burp suite 
# proxies = {
#     "http": "**************",
#     "https": "*************
# }

# r.proxies.update(proxies)
# r.verify = False 

# getting phone number 
phone_number = input("enter your Iranian number: ")

# getting login http packet 
packet = {
    "backurl": "/",
    "username": phone_number, 
    "otp_call": False
}

# login with our packet 
res = r.post('https://api.digikala.com/v1/user/authenticate/',
             headers={"Content-Type": "application/json"},
             data=json.dumps(packet))

# checking if first step was successfull -> continue 
if res.status_code == 200:
    print(f"status code is {res.status_code}\n+--sending otp code to +98{phone_number}")

    otp_code = input(f"enter ur otp code sent to {phone_number}: ") # getting otp code 

    # getting new otp packet 
    otp_packet = {
        "backurl": "/",
        "type": "otp", 
        "username": phone_number,
        "code": otp_code
    }

    # finnish the login proccess with otp code 
    r.post('https://api.digikala.com/v1/user/login/otp/',
           headers={"Content-Type": "aplication/json"},
           data=json.dumps(otp_packet)
    )

    print(res.status_code, res.text) # print the result 

