

import sys 

name = input("Enter name: ") 

mobile = input("Enter mobile number: ") 

email = input("Enter email address: ") 

address = input("Enter physical address: ") 

# create vcard 
vcard = open(name+".vcf","w") 
vcard.write("BEGIN:VCARD\nVERSION:3.0\n") 
vcard.write("N:"+name+"\n") 
vcard.write("TEL;TYPE=CELL:"+mobile+"\n") 
vcard.write("EMAIL:"+email+"\n") 
vcard.write("ADR:"+address+"\n") 
vcard.write("END:VCARD") 

vcard.close() 

print(name+"\'s vCard saved!")