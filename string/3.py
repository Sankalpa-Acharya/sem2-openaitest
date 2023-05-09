

def check(string1, string2): 
    if(string1 in string2): 
        print("Yes, string1 is a substring of string2") 
    else: 
        print("No, string1 is not a substring of string2") 
      
  
string1 = "hello"
string2 = " world hello"
check(string1, string2)