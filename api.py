import requests


url = str(input("★ Give The Site Search URL:"))

svlu = str(input("★ Enter Search Keyword:"))

amn = int(input(" ★ Enter Amount Of Request: "))

rmt = int(input("★ Select Request Method (get = 1 /post = 2)"))

value = {"number": svlu}

if(rmt == 1):
          for i in range(amn):
    
                  requests.get(url, data=value)
                  print(str(i+1)+" Requests SEND SUCCESSFULLY (°-°) DV: HOX**R - TALHA - Get")
         
if(rmt == 2):
         for i in range(amn):
    
                 requests.post(url, data=value)
                 print(str(i+1)+" Requests SEND SUCCESSFULLY (°-°) DV: HOX**R - TALHA - Post")
         
