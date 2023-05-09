
api = ""

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import os
import openai
import json
openai.api_key = api
fileio=[
    "Write a program to create a csv file that we can directly open in MS-Excel.",
    "Read the data stored in MS-Excel file and convert it into a dictionary. The record contains rollno, name of student, marks of three subjects. Also calculate total. Display the dictionary data on the monitor.",
    "Accept contact details from the user and create a vcard that we can directly store in our mobile.",
    "Create a specific subdirectory and copy one file from another subdirectory to this newly created subdirectory.",
    "Write a program to copy contents of one file to another. While doing so, replace all lowercase characters into uppercase characters.",
    "Write a program that merges lines alternatively from two files and writes the results to new file. If one file has less number of lines than the other,  the remaining lines from the larger file should be simply copied into the target file.",
    "If an Employee object contains following details: empcode, empname, Date of Joining, Salary Write a program to serialize and deserialize this data.",
    "Given a text file, write a program to create another text file deleting the words ‘a’, ‘the’, ‘an’ and replacing each one of them with a blank space."
]


def openaiAnswer(question):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"{question}",
        temperature=0.9,
        max_tokens=1063,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    text = json.loads(json.dumps(response['choices']))[0]['text']
    return text
count = 0 
for i in fileio:
    print(i)
    count +=1
    with open(f'./normal/{count}.py','w') as f:
        f.write(openaiAnswer("write python code"+i+", i only need code without output with proper formatting"))

