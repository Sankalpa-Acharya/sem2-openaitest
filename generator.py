
api = ""

# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import os
import openai
import json
openai.api_key = api
string = [
    "Count how many vowels are there in a string. Accept the string from the user.",
    "Write your own functions (without using built-in functions) to convert all characters of a string into lower case/upper case/toggle case.",
    "Accept two strings. Check whether one string is there in another string.",
    "Write a function that removes one string from another string, if present. E.g. Onestring = “abcdef”, removestring = “cd”. The finalstring should contain “abef”."
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
for i in string:
    print(i)
    count +=1
    with open(f'./normal/{count}.py','w') as f:
        f.write(openaiAnswer("write python code"+i+", i only need code without output with proper formatting"))

