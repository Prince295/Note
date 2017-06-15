# -*- coding: cp1251 -*-
import pickle
import re
from datetime import datetime

try:
    with open('Dump.dat', 'rb') as dump_in:
        notes = pickle.load(dump_in)
except EOFError:
        notes={}

def reminder():
    date = datetime.strftime(datetime.now(), "%Y.%m.%d")
    da = date.split('.')
    try:
        keys = notes.keys()
        for i in range(len(notes)):
            DateOfBirth = notes[keys[i]]['Date of birth']
            list = DateOfBirth.split('/')
            if da[1] == list[1] and da[2] == list[0]:
                print "Time to congratz - " + keys[i] + "!   Today is his Birthday, don't forget to call him - his number is: " + str(notes[keys[i]]['Phone'])
    except AttributeError:
        keys =[]
    return

def main(notebook,reminder):
    reminder()
    while True:
        x=raw_input("Enter 'E', if you wanna make new note, or 'F', if wanna find smbdy ")
        if x=='E' or x=='e':
            new_notes=notebook(notes)
            with open('Dump.dat', 'wb') as dump_out:
                pickle.dump(new_notes, dump_out)
            break
        if x=='F' or x=='f':
            find(notes)
            break
        print("You doesn't enter command. Plz enter 'E' or 'F'")

    return notes


def notebook(notes):

    while True:
        name = raw_input("Enter Name(only letters and numbers): ")
        name_check=name.replace(' ', '')
        if name_check.isalnum() and (0<len(name)<255):
            break
        else:
            print("Incorrect enter, please try again")
    while True:
        phone = raw_input("Enter phone(format:first number 8 or 9, max lenght - 10 symbols) : ")
        if re.match(r'[8-9]{1}[0-9]{0,9}', phone) and (len(phone) <= 11):
            break
        else:
            print("Incorrect number, please try again")
    while True:
        dateOfBirth = raw_input("Enter date of Birth(format DD/MM/YYYY): ")
        if re.findall(r'\d{2}\/\d{2}\/\d{4}\b', dateOfBirth)!=[]:
            break
        else:
            print("Incorrect data, please try again")
    if notes == '':
        notes = {name:{'Name': name, 'Phone': str(phone), 'Date of birth': str(dateOfBirth)}}
    else:
        notes[name]={'Name': name, 'Phone': str(phone), 'Date of birth': str(dateOfBirth)}
    return notes


def find(notes):
    key = raw_input("Enter name, witch you wanna search, or part of name: ")
    try:
        keys = notes.keys()
    except AttributeError:
        keys = []
    i=0
    answerlist=[]
    while i < len(keys):
        if key == keys[i]:
            answer = 'Name: ' + str(keys[i]) + ' Phone: ' + str(notes[keys[i]]['Phone']) + ' Date Of Birth: ' + str(notes[keys[i]]['Date of birth'])
            print answer
        else:
            if re.match(key, keys[i]):
                answer = 'Name ' + str(keys[i]) + ' Phone ' + notes[keys[i]]['Phone'] + ' Date Of Birth ' + notes[keys[i]]['Date of birth']
                answerlist.append(answer)
        i+=1
    if len(answerlist)>0:
        print answerlist
    else:
        print "No matches"
print main(notebook,reminder)
raw_input()