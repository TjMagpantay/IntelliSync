'''
Welcome to IntelliSync - Our Chatbot name is Mechamaru, a friendly chatbot buddy here to assist user in this program!.
This ChatBot is designed to engage in conversation with user and provide responses based on the input they provide.
Whether they have questions, need advice, or just want to chat, feel free to enter your inquiries.

GROUP MEMBERS:
Tammy Jane Magpantay
King Cedrick Panaligan
Lourenz Angel Francisco
John Adrian Perce
Marife Fraulein Rollon
Keith Andrei Ciruelas
Michael Gonzales
'''

import re
from urllib import response
import chatbot
import long_responses as long


def get_response(user_input):
    # Add your message probability and response logic here
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = chatbot.check_all_messages(split_message)
    return response

def main_chat():
    # Main conversation loop
    while True:
        user_input = input('\nYou: ')
        response = get_response(user_input)
        print('\nMechamaru: ' + response)

        # You can add additional exit conditions here if needed
        if any(word in user_input.lower() for word in ['bye', 'goodbye']):
            print('\nMechamaru: I will now exit the conversation.')
            break
