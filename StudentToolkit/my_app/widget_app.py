from my_app import app
from flask import render_template, request, redirect, url_for
import requests
import random


@app.route("/password_generator")
def random_password_generator():
    letters = "abcdefghijklmnopqrstuvwxyz"
    characters = letters + letters.upper()
    numbers = "0123456789"
    characters += numbers
    symbols = "!@#$%^&*()-=_+;':\",./<>?`~|\\"
    characters += symbols
    password = ""
    for x in range(15):
        password += random.choice(characters)
    return render_template('password.html', random_password=password)



@app.route("/remove_formatting")
def remove_formatting():
    return render_template('remove_formatting.html')

@app.route("/remove_formatting", methods=['POST'])
def my_form_post1():
    text = request.form['text']
    processed_text = str(text)
    return render_template('remove_formatting.html', formatted_text = processed_text)



def remove_leading_and_trailing_whitespace(text):
    text = str(text)
    text = text.split("\n")
    for i in range(len(text)):
        text[i] = text[i].strip()
    return "\n".join(text)

@app.route("/remove_leading_and_trailing_whitespace")
def whitespace():
    return render_template('whitespace.html')

@app.route("/remove_leading_and_trailing_whitespace", methods=['POST'])
def my_form_post2():
    text = request.form['text']
    processed_text = remove_leading_and_trailing_whitespace(text)
    return render_template('whitespace.html', no_whitespace = processed_text)



def word_counter(text):
    text = remove_leading_and_trailing_whitespace(text)
    text = text.split(" ")
    return (len(text))

@app.route("/word_counter")
def counter():
    return render_template('word_counter.html')

@app.route("/word_counter", methods=['POST'])
def my_form_post3():
    text = request.form['text']
    processed_text = word_counter(text)
    return render_template('word_counter.html', word_count = processed_text)
    
    
    
def sarcasm(text):
    text = list(text)
    x = 0
    for i in range(len(text)):
        text[i] = text[i].lower() if x%2==0 else text[i].upper()
        x += 1
    return "".join(text)

@app.route("/sarcasm")
def sarcasm_in():
    return render_template('sarcasm.html')

@app.route("/sarcasm", methods=['POST'])
def my_form_post4():
    text = request.form['text']
    processed_text = sarcasm(text)
    return render_template('sarcasm.html', sarcastic_text = processed_text)
