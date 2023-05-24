#!/usr/bin/env python
# coding: utf-8
import speech_recognition as sr
import pyttsx3
import os
import time
import subprocess
import win32com.client as wincl
import openai
import datetime

speak = wincl.Dispatch("SAPI.SpVoice")
openai.api_key = "<your API Key>"

# Function to get user's name
def get_username():
    repo_path = 'test'
    os.chdir(repo_path)
    if os.path.exists("username.txt"):
        with open("username.txt", "r") as f:
            username = f.read().strip()
    else:
        with sr.Microphone() as source:
            print("Hi, what's your name?")
            speak.Speak("Hi, what's your name?")
            audio = r.listen(source)
            try:
                username = r.recognize_google(audio)
            except sr.UnknownValueError:
                username = "User"
        with open("username.txt", "w") as f:
            f.write(username)
    print(f"Hello, {username}!")
    speak.Speak(f"Hello, {username}!")
    print("metahiber is awake now")
    speak.Speak("metahiber is awake now")
    return username

# Function to create the "codes" folder
def create_codes_folder():
    if not os.path.exists("test"):
        print("creating folderrrrrrrrrrrrrrrrrr")
        os.mkdir("test")
    # else:
    #     repo_path = 'test'
    #     os.chdir(repo_path)

# Function to generate a unique filename
def generate_filename(file_extension):
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d_%H-%M-%S") + file_extension

# Get user's name
r = sr.Recognizer()
username = get_username()

# Add an "awake word" to activate the chatbot
awake_word = "metahiber"

# Create the "codes" folder
#create_codes_folder()
message="meta"
while message.lower!="bye":
    #print("inside while loop...")
    message=" "
    with sr.Microphone() as source:
        #print(f"{username}, how can I assist you?")
        #speak.Speak(f"{username}, how can I assist you?")
        print("i am listening.....")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,timeout=10)
        try:
            message = r.recognize_google(audio)
        except sr.UnknownValueError:
            message = ""
        except sr.WaitTimeoutError:  # handle the timeout error
            print("Timeout occurred, waiting for awake word...")
            speak.Speak("Timeout occurred, waiting for awake word...")
            continue  # continue with the loop without executing the code below

        print(f"{username}: {message}")
    if "bye" in message.lower():
        # Exit the program
        print("Goodbye!")
        speak.Speak("Goodbye!")
        break    
    # Check if the awake word was spoken
    #if awake_word in message.lower() or "meta" in message.lower() or "hiber" in message.lower() or "hyper" in message.lower():
    if True:
        #print("metahiber is awake now")
        # with sr.Microphone() as source:
        #     #print(f"{username}, how can I assist you?")
        #     #speak.Speak(f"{username}, metahiber is awake now")
        #     print("i am listening.....456")
        #     audio = r.listen(source)
        #     try:
        #         message = r.recognize_google(audio)
        #     except sr.UnknownValueError:
        #         message = ""
        #     print(f"{username}: {message}")
            #print(len(message))
        # Check if the user wants to write some code
        if "code" in message.lower():
            #print("inside coding")
            # Generate a unique filename and create the file in the "codes" folder
            # Ask the user to dictate the code
            print(f"{username}, please dictate the code.")
            speak.Speak(f"{username}, please dictate the code.")
            with sr.Microphone() as source:
                print("i am listening.....")
                audio = r.listen(source)
            code = r.recognize_google(audio)
            code="You're a web developer who has been tasked with creating a website for a Harry Potter fan community., as well as a form for users to join the community. How would you design and build this website? Write complete html code and considerations to ensure that the website is visually appealing, user-friendly, and meets the needs of the Harry Potter fan community. It should also have js where text should be animated background should be black."
            print(code)
            if("html" in code.lower()):
                file_extension=".html"
            elif("python" in code):
                file_extension=".py"
            else:
                file_extension=".txt"
            print(subprocess.getoutput("dir"))
            #repo_path = 'test'
            #os.chdir(repo_path)
            filename = os.path.join(".", generate_filename(file_extension))
            with open(filename, "w") as f:
                #try:
                if(True):
                    response = openai.Completion.create(
                        engine="text-davinci-003",
                        prompt=code,
                        max_tokens=1000,
                    )
                    response_code = response.choices[0].text.strip()
                    print(response_code)
                    f.write(response_code)
            print(f"{username}, your code has been saved in {filename}.")
            speak.Speak(f"Your code has been saved in {filename}.")
            cmd1 = ['git', 'add', '.']
            print(subprocess.run(cmd1, cwd='.'))
            cmd2 = ['git', 'commit', '-m', 'new changes...']
            output=subprocess.run(cmd2, cwd='.')
            print(output)
            #repo_path = 'test'
            #os.chdir(repo_path)
            subprocess.run(['git', 'push'])
            speak.Speak("Code is succesfully pushed to the Github repo")
            speak.Speak("Code deployed Succesfully!")
#                 except:
#                     print("Sorry, I could not understand your code.")
#                     speak.Speak("Sorry, I could not understand your code.")
            # Run the "git push" command
            #subprocess.run(["git", "push"])
        elif(len(message)!=0):
            # print(len(message))
            # print(message)
            # print(type(message))
            # print(len(message)!=0)
            # print("inside normal task..............")
            # Ask GPT-3 for a response
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=message,
                    max_tokens=100,
                )
                response_text = response.choices[0].text.strip()
                print("ChatGPT:", response_text)
                speak.Speak(response_text)
            except:
                print("error comuniting with openAI")
                speak.Speak("error comuniting with openAI")
        #message = ""
