!git clone https://github.com/gunthercox/ChatterBot.git
%cd ChatterBot
!pip install -e .
!pip install chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
print("ChatterBot is working on Colab!")
trainer = ListTrainer(healthify)
conversations = [
    'Hi',
    'Hello! I am HealthBot. How can I assist you today?',
    'Hello',
    'Hi! Do you have a health-related question?',
    'I have a headache',
    'You should rest, stay hydrated, and take a mild pain reliever if needed.',
    'What should I do if I have a fever?',
    'Drink plenty of fluids and rest. If the fever persists, please consult a doctor.',
    'I feel dizzy',
    'Sit down, breathe deeply, and drink water. If it continues, seek medical help.',
    'What should I eat for a cold?',
    'Warm fluids, soups, citrus fruits, and light meals help during a cold.',
    'How to stay healthy?',
    'Eat balanced meals, exercise regularly, stay hydrated, and get enough sleep.',
    'What should I do in case of a cut?',
    'Clean the wound with water, apply antiseptic, and cover it with a clean bandage.',
    'How much water should I drink daily?',
    'Generally, 2 to 3 liters per day is recommended, but it varies based on your activity.',
    'Thank you',
    'You’re welcome! Take care.',
    'Bye',
    'Goodbye! Stay healthy.'
]
print("Ask something to Healthify (type 'exit' to end):\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Healthify: Bye! Stay healthy.")
        break
    response = healthify.get_response(user_input)
    print(f"Healthify: {response}")
!pip install textblob
import nltk
nltk.download('punkt')
from textblob import TextBlob
print("Ask something to Healthify (type 'exit' to end):\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Healthify: Bye! Stay healthy.")
        break
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity
    if polarity < -0.3:
        prefix = "I'm sorry you're feeling that way. "
    elif polarity > 0.3:
        prefix = "That's great to hear! "
    else:
        prefix = ""
    response = healthify.get_response(user_input)
