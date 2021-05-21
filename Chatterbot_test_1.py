from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
my_bot = ChatBot("Nova")
small_talk = ['Hi there!', 'Hi!', 'Hello.', 'I am good.', 'I am happy.']
trainer = ListTrainer(my_bot)
trainer.train(small_talk)
s = "Hi"
print(my_bot.get_response(s))

#use this code in colab.research.google.com