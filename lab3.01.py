'''
##############
Lab 3.01
##############
1.  Practice importing random** — Use randint with different arguments. Simulate a dice roll, printing out to the user what number they rolled.

2.  Look at the documentation of the random library — Experiment with another function (not randint) that returns a value.

3.  Create a program that simulates a magic 8-ball​
    1.  Store all of the 8-ball's possible responses (shown below) in a list

    2.  Have the program prompt the user to ask the magic 8-ball a question

        then return and print a random response.

Magic 8-Ball Response Examples
Outlook is good

Ask again later

Yes

No

Most likely no

Most likely yes

Maybe

Outlook is not good
'''
import random

resp = ['Ask again later', 'Yes', 'No', 'Most likely no', 'Most likely yes', 'Maybe', 'Outlook is not good']


while True:
    question = input("I am the magic 8-ball. You may ask me anything: ")
    print(resp[random.randint(0, len(resp)-1)])