"""
Date : 11-07-2019
"""


def whatismyname():

    fname = input("What is your firstname? - ")
    lname = input("What is your lastname? - ")
    if len(fname) >=10 or len(lname) >= 10:
        print("Firstname or lastname should not exceed length of 10 char ")
    else:
        print("Hello " + fname + lname + "! You just delved into python")

whatismyname()
