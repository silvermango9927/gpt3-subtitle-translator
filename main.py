from dotenv import dotenv_values
import openai
import time
import streamlit as st


vals = dotenv_values(".env")
openai.api_key = vals['OPENAI_API_KEY']


str = input('Enter the language you wish to see the transcript in : ')
translation=[]

with open('transcript.srt', 'r') as f:
    data = f.readlines()
    # print(data)
    for d in data:
        # print(d)
        c=d.split('\n\n')
        if c[0][0].isalpha():
            # print(c[0])
            prompt = "Translate the following text to {language} : {text}".format(language=str, text=c[0].replace('\n', ' '))            
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.7,
                max_tokens=1256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            for choice in response['choices']:
                sum=(choice['text'])
                translation.append(sum)
# print(translation)

# Writing out the translations in the same format as transcript.srt into another srt file
translated_data = []
with open('transcript.srt', 'r') as f:
    data = f.readlines()
    i=0
    for d in data:
        c=d.split('\n\n')
        if c[0][0].isalpha():
            c[0]=translation[i]
            i+=1
        c='\n\n'.join(c)
        translated_data.append(c)

print(translated_data)
with open('translation.srt', 'w') as f:
    f.writelines(translated_data)
