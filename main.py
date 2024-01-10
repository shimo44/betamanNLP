import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections
from nltk.corpus import words
import random
import nltk
nltk.download('punkt')
nltk.download('words')


class ChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("BETAMAN.EXE")

        self.chat_log = scrolledtext.ScrolledText(self.window, state='disabled')
        self.chat_log.pack(side="top", fill="both", expand=True)

        self.message_entry = tk.Entry(self.window, width=100)
        self.message_entry.pack(side="left", padx=10, pady=10)

        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack(side="left", padx=10, pady=10)

    def run(self):
        self.window.mainloop()

    def chatbot_response(self, user_input):
        # Define the chatbot responses
        responses = [

            # English
            (r'hello|hi|hey', ('Hi there!', 'Hello!', 'Hey!')),
            (r'what is your name\??', ('My name is Betaman..', 'They call me Betaman!')),
            (r'who are you|what are you\??', ('My primary function is to chat! Hi', 'I\'m a Chatbot and Friend of Daichi Shimo!')),
            (r'how are you\??', ('I\'m doing well, thank you for asking.', 'I\'m good, how about you?')),
            (r'goodbye|bye|see you', ('Goodbye!', 'Take care!')),
            (r'school|classes|homework',
             ('How was school today?', 'Did you have a lot of homework?', 'What subjects do you enjoy the most?')),
            (r'friends|bff|best friend', ('Tell me more about your friends.', 'Do you have a best friend?',
                                          'What do you like to do with your friends?')),
            (r'music|bands|concerts', ('What kind of music do you like?', 'Have you been to any concerts recently?',
                                       'Who are your favorite bands?')),
            (r'tv shows|movies|netflix', (
            'What are your favorite TV shows or movies?', 'What have you been watching on Netflix?',
            'Have you seen any good movies recently?')),
            (r'sports|fitness|exercise',
             ('What sports do you play or watch?', 'Do you enjoy exercising?', 'How do you like to stay active?')),
            (r'games|video games|board games', (
            'What games do you enjoy playing?', 'Do you prefer video games or board games?',
            'What is your favorite video game?')),
            (r'holidays|vacations|travel',
             ('Where have you traveled to?', 'What is your favorite holiday?', 'What is your dream vacation?')),
            (r'food|restaurants|cooking', ('What is your favorite type of food?', 'Do you enjoy cooking?',
                                           'What are some of your favorite restaurants?')),
            (r'books|reading|writing',
             ('What books have you read recently?', 'Do you enjoy writing?', 'What is your favorite book?')),
            (r'anxiety|panic|stress', (
            'It sounds like you may be experiencing anxiety or stress. Can you tell me more about what you\'re feeling?',
            'It\'s common to feel anxious or stressed in certain situations. What\'s been going on lately?')),
            (r'depression|sadness|hopeless', (
            'It sounds like you may be feeling down or depressed. Can you tell me more about what\'s been going on?',
            'Depression can be a difficult experience. How long have you been feeling this way?')),
            (r'trauma|PTSD|flashback', (
            'It sounds like you may be experiencing symptoms related to trauma. Have you had any traumatic experiences in the past?',
            'It\'s not uncommon for traumatic experiences to affect our mental and emotional well-being. Can you tell me more about what you\'ve been experiencing?')),
            (r'relationships|family|friends', (
            'Relationships with others can be complex and challenging. Can you tell me more about the relationships in your life?',
            'It sounds like you may be experiencing some difficulties in your relationships. How have your relationships been going lately?')),
            (r'lonely|isolated|alone', (
            'Feeling lonely or isolated can be difficult. Can you tell me more about what\'s been going on?',
            'It\'s not uncommon to feel lonely or isolated at times. Have you been feeling this way for long?')),
            (r'self-esteem|confidence|self-worth', (
            'It sounds like you may be struggling with your self-esteem. Can you tell me more about how you\'re feeling?',
            'Self-esteem can be a challenging issue. How have you been feeling about yourself lately?')),
            (r'coping|resilience|stress management', (
            'Coping and stress management are important skills to develop. What strategies have you used in the past to cope with stress?',
            'Building resilience can be helpful in managing stress. Are there any activities or techniques you find helpful in managing stress?')),
            (r'boundaries|self-care|assertiveness', (
            'Setting boundaries and practicing self-care can be important for our well-being. How do you currently prioritize your own needs?',
            'Assertiveness can be a helpful skill in maintaining healthy boundaries. Can you tell me more about a situation where you\'ve had to be assertive?')),

            # Japanese
            (r'こんにちは', ('こんにちは！', 'どうも')),
            (r'元気ですか\??', ('はい、元気です。', 'おかげさまで')),
            (r'おはよう', ['おはようございます！']),
            (r'今日は何をしましたか？', ['今日は仕事に行ってきました。']),
            (r'明日の天気はどうですか？', ['明日は晴れる予定です。']),
            (r'ありがとう', ['どういたしまして。']),
            (r'さようなら', ['さようなら。またお話しましょう！']),
            (r'.*', ['すみません、よくわかりませんでした。'])
        ]

        # Create the chatbot
        chatbot = Chat(responses, reflections)

        # Get the chatbot response to the user input
        chatbot_response = chatbot.respond(user_input)

        return chatbot_response

    def send_message(self):
        message = self.message_entry.get()
        self.message_entry.delete(0, 'end')
        self._update_chat_log("You: " + message)

        # Call your chatbot API or function to get the response
        chatbot_response = self.chatbot_response(message)

        self._update_chat_log("Betaman: " + chatbot_response)

    def _update_chat_log(self, message):
        self.chat_log.configure(state='normal')
        self.chat_log.insert('end', message + '\n')
        self.chat_log.configure(state='disabled')
        self.chat_log.yview('end')


if __name__ == '__main__':
    gui = ChatbotGUI()
    gui.run()
