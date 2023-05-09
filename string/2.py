

def convert_lower(word): 
  
    # Get the ascii number of  
    # character and add 32 to  
    # make it lower case 
    lower = chr(ord(word) + 32) 
      
    return lower 
  
def convert_upper(word): 
      
    # Get the ascii number of  
    # character and subtract 32 to 
    # make it upper case 
    upper = chr(ord(word) - 32) 
    return upper 
  
def toggle_case(word): 
  
    # Get the ascii number of character 
    ascii_num = ord(word) 
  
    # If character is in upper case, 
    # convert it to lower case 
    if ascii_num >= 65 and ascii_num <= 90: 
        return chr(ascii_num + 32) 
  
    # If character is in lower case, 
    # convert it to upper case 
    else: 
        return chr(ascii_num - 32)