"""

Date : 22-07-2019
Author: Dhruvik Mevada ( dhruvik333@gmail.com )

Sample input:

    Enter firstname: dhruvik
    Enter lastname: mevada
    Enter Company Domain : cybersky.com

Sample output:

    Your company Email: dhruvik.mevada@cybersky.com
    Your Password: MrYQIiUS

"""


import random


class email_and_passwordgen():

    def __init__(self):

        self.first_name = input("Enter firstname: ")
        self.last_name = input("Enter lastname: ")
        self.comp_domain = input("Enter Company Domain : ")

    def comp_email(self):

        # Taking the firstname and lastname as list elements and joining them to create email address
        compemail = ''.join([self.first_name, ".", self.last_name, "@", self.comp_domain])
        print("Your company Email: " + compemail)

    def passgen(self):

        # Taking string containing all alphabets, digits and special symbols.
        passwd = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*."
        # password length
        passlen = 8
        final_passwd = ''.join(random.sample(passwd,passlen))
        print("Your Password: " + final_passwd)


if __name__ == '__main__':
    a = email_and_passwordgen()
    a.comp_email()
    a.passgen()
