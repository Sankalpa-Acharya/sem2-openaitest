

def mergefiles(file1, file2): 
    with open(file1) as f1, open(file2) as f2: 
        while True: 
            line1 = f1.readline() 
            line2 = f2.readline() 
            # check if line1 is not empty 
            if line1: 
                yield line1.rstrip('\n') 
  
            # if line2 is not empty 
            if line2: 
                yield line2.rstrip('\n') 
  
            # check if both lines are empty 
            if not line1 and not line2: 
                break
  
# Driver Code 
with open('output.txt', 'w') as target: 
    for line in mergefiles('input1.txt', 'input2.txt'): 
        target.write(line + '\n')