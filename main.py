"""This module is created to comfortably navigate through json file"""
import json
from pprint import pprint


def read_json_file():
    """
    Asks the user to enter path of json file
    Reads this file and converts json extension to dict or list
    :return: python object
    """
    file = input("Enter path to json file:\n")
    with open(file, encoding='utf-8', errors='ignore') as json_data:
        return json.load(json_data, strict=False)


def navigate_through_file(data):
    """
    Navigates the user through the file
    :return:
    """
    while True:
        if isinstance(data, dict):
            print("This is a dictionary. Do you want to see all the keys?\n")
            answer = input()
            if answer == 'q':
                quit()
            elif answer.lower() == 'yes':
                if len(data) == 0:
                    print("This dictionary is empty. Nothing to display.")
                    quit()
                else:
                    pprint(data.keys())
                    print("Enter a key to see the info.\n")
                    answer = input()
                    if not data[answer]:
                        print("There is no such key in this dictionary,\n"
                              "try picking one from the list:\n")
                        pprint(data.keys())
                    else:
                        pprint(data[answer])
                        data = data[answer]
            elif answer.lower() == 'no':
                print("Enter a key in this dictionary that you want to see.\n")
                answer = input()
                if not data[answer]:
                    print("There is no such key in this dictionary,\n"
                          "try picking one from the list:\n")
                    pprint(data.keys())
                else:
                    pprint(data[answer])
                    data = data[answer]
            else:
                print("Please, print yes or no, or print 'q' if you wish to quit.\n")
        elif isinstance(data, list):
            print("This is a list. Do you want to see it all?\n")
            answer = input()
            if answer == 'q':
                quit()
            elif answer.lower() == 'yes':
                pprint(data)
            elif answer.lower() == 'no':
                print("Enter an index in range from 0 to 9")
                answer = int(input())
                try:
                    print(data[answer])
                except IndexError:
                    print("The index is not correct.\n")
        elif isinstance(data.values(), str):
            print("This is a string. Do you want to display it?\n")
            answer = input()
            if answer == 'q':
                quit()
            elif answer.lower() == 'yes':
                if len(data.values()) == 0:
                    print("This list is empty. Nothing to display.\n")
                    quit()
                print(data.values())
                print("This is the end of this file.\n")
            else:
                print("Thank you for using our program. Come back soon.\n")
                quit()
        else:
            print("Please, print yes or no, or print 'q' if you wish to quit.\n")
