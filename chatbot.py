import re
import random
import long_responses as long
from main import main_chat

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Checks if each recognized word is present in the user message
    for word in recognised_words:
        if word in user_message:
            message_certainty += 1

    # Calculates the percent of recognized words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dictionary
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello there! How can I assist you today?', ['hello', 'hi', 'hey', 'sup', 'heyo'],
             single_response=True)
    response('Thanks for the conversation!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code'], required_words=['love'])
    response('Sorry:(', ['hate', 'not'], single_response=True)
    response('Good morning too!', ['good', 'morning'], required_words=['morning'])
    response('Good afternoon too!', ['good', 'afternoon'], required_words=['afternoon'])
    response('Good evening too!', ['good', 'evening'], required_words=['evening'])
    response("I'm a bot, not a human, so I don't experience emotions.", ['feel', 'emotion',
                                                                         'emotional'], required_words=['emotion'])
    response("Programming languages? I know quite a few. What's your favorite?",
             ['favorite', 'programming', 'language'])
    response("I'm constantly learning and updating. Ask me anything!", ['learn', 'update',
                                                                        'knowledge'], required_words=['update'])
    response("I'm here 24/7. Is there anything else you'd like to chat about?", ['chat', 'talk',
                                                                                 'anything'], required_words=['chat'])
    response("I don't sleep, but I'm always here to chat. What's on your mind?", ['sleep', 'rest',
                                                                                  'mind'], required_words=['sleep'])


    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['you', 'eat', 'eaten'], required_words=['you', 'eaten'])
    response(long.R_JOKE, ['give', 'joke'], required_words=['joke'])
    response(long.R_JOKE2, ['give', 'another', 'joke'], required_words=['another', 'joke'])
    response(long.R_HELP, ['please', 'question', 'answer'], required_words=['answer'])
    response(long.R_HELP2, ['please', 'question', 'answer'], required_words=['need', 'help'])
    response(long.R_PYTHON_BASICS, ['python', 'basics', 'learn', 'variables', 'loops', 'functions'],
             required_words=['python'])
    response(long.R_FAVORITE_LANGUAGE, ['python', 'favorite', 'language'], required_words=['python'])
    response(long.R_PYTHON_LIBRARIES, ['python', 'libraries', 'numpy', 'pandas', 'matplotlib'],
             required_words=['python'])
    response(long.R_COMPUTER_HISTORY, ['computer', 'history', 'Ada Lovelace', 'Charles Babbage'],
             required_words=['computer'])
    response(long.R_CODING_TIPS, ['coding', 'tip', 'break down', 'problems'], required_words=['coding'])
    response(long.R_VIRTUAL_ENVIRONMENT, ['python', 'projects', 'virtual environments', 'dependencies'],
             required_words=['python'])
    response(long.R_TEXT_EDITOR, ['coding', 'python', 'text editor', 'VSCode', 'Sublime Text'],
             required_words=['coding'])
    response(long.R_PYTHON_FRAMEWORKS, ['python', 'frameworks', 'Django', 'Flask'], required_words=['python'])
    response(long.R_DEBUGGING, ['debugging', 'programming', 'print statements', 'debugging tools'],
             required_words=['debugging'])
    response(long.R_VERSION_CONTROL, ['version control', 'Git', 'collaborative coding'],
             required_words=['version control'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Introduction
print("_________________________________________________________________________________________________________________")
print("|                                       Welcome to IntelliSync!                                                 |")
print("|                                                                                                               |")
print("|Meet Mechamaru, your friendly chatbot buddy here to assist you in this program!. This ChatBot is designed to   |"
      "\n|engage in conversation with you and provide responses based on the input you provide. Whether you have         |"
      "\n|questions, need advice, or just want to chat, feel free to enter your inquiries.                               |")
print("|                                                                                                               |")
print("|How to sUse:                                                                                                    |")
print("|  1.Enter Your Inquiry: Type your message or question in the input prompt, and Mechamaru will respond          |"
      "\n|  accordingly.                                                                                                 |")
print("|  2.Terminating the Program: To exit the ChatBot, simply type \"bye\" or \"goodbye\" (case insensitive). This      |"
      "\n|  will end the conversation and terminate the program.                                                         |")
print("|_______________________________________________________________________________________________________________|")
# Ask the user if they want to use the chat bot
while True:
    user_decision = input("\nDo you want to use the ChatBot? (yes/no): ").lower()
    print("****************************************************************************************************************")
    if user_decision == 'yes':
        main_chat()  # Call the main_chat function from main_chatbot.py
        break
    elif user_decision == 'no':
        print("Goodbye! If you change your mind, feel free to come back.")
        exit()
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
