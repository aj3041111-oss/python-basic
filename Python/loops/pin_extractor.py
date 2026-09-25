import re

text = input("Enter text: ")

pins = re.findall(r'\b\d{4}\b', text)

print("PINs Found:")
for pin in pins:
    print(pin)
    
# EMAIL 
message = "Dear User, your verification PIN is 8392. Do not share it."

import re

pin = re.search(r'\d{4}', message)

if pin:
    print("PIN:", pin.group())
else:
    print("No PIN found")    