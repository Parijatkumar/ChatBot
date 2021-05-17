from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


bot = ChatBot('ChatBot')
bot.set_trainer(ListTrainer)
#you = pyttsx3.init()

conversation = open('chat.txt', 'r').readlines()   # alt-up and alt-down moves for method

bot.train(conversation)
name = input(" ChatBot :what is your name-")
while True:
    message = input(name + ':')
    if message.strip() != 'bye':
        reply = bot.get_response(message)
      # you.say(reply)
        print('chatbot:', reply)
       #S you.runAndWait()
    if message.strip() == 'bye':
        print('ChatBot:Bye')
        break
