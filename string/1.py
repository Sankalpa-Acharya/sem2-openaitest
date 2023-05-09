

vowel=0
st=input("Enter any string")
for i in st:
      if(i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U'):
            vowel=vowel+1
print("There are",vowel,"vowels in the given string.")