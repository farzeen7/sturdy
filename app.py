import nltk
import numpy as np
import random
import string

import bs4 as bs
import urllib.request
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



raw_html = urllib.request.urlopen('https://en.wikipedia.org/wiki/Tennis')
raw_html = raw_html.read()

article_html = bs.BeautifulSoup(raw_html, 'lxml')

article_paragraphs = article_html.find_all('p')

article_text = ''

for para in article_paragraphs:
    article_text += para.text

article_text = article_text.lower()

article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)

article_sentences = nltk.sent_tokenize(article_text)
article_words = nltk.word_tokenize(article_text)


wnlemmatizer = nltk.stem.WordNetLemmatizer()

def perform_lemmatization(tokens):
    return [wnlemmatizer.lemmatize(token) for token in tokens]

punctuation_removal = dict((ord(punctuation), None) for punctuation in string.punctuation)

def get_processed_text(document):
    return perform_lemmatization(nltk.word_tokenize(document.lower().translate(punctuation_removal)))

greeting_inputs = ("hey", "good morning", "good evening", "morning", "evening", "hi", "whatsup")
greeting_responses = ["hey", "hey hows you?", "*nods*", "hello, how you doing", "hello", "Welcome, I am good and you"]

def generate_greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in greeting_inputs:
            return random.choice(greeting_responses)

def generate_response(user_input):

    ChatterBox_response = ''
    article_sentences.append(user_input)

    word_vectorizer = TfidfVectorizer(tokenizer=get_processed_text, stop_words='english')
    all_word_vectors = word_vectorizer.fit_transform(article_sentences)
    similar_vector_values = cosine_similarity(all_word_vectors[-1], all_word_vectors)
    similar_sentence_number = similar_vector_values.argsort()[0][-2]

    matched_vector = similar_vector_values.flatten()
    matched_vector.sort()
    vector_matched = matched_vector[-2]

    if vector_matched == 0:
        ChatterBox_response = ChatterBox_response + "I am sorry, I could not understand you"
        return ChatterBox_response
    else:
       ChatterBox_response = ChatterBox_response + article_sentences[similar_sentence_number]
       return ChatterBox_response


word_vectorizer = TfidfVectorizer(tokenizer=get_processed_text, stop_words='english')
all_word_vectors = word_vectorizer.fit_transform(article_sentences)
similar_vector_values = cosine_similarity(all_word_vectors[-1], all_word_vectors)
similar_sentence_number = similar_vector_values.argsort()[0][-2]



continue_dialogue = True
print("Hello, I am your friend ChatterBox.how can i help you:")
while(continue_dialogue == True):
    human_text = input()
    human_text = human_text.lower()
    if human_text != 'bye':
        if  human_text == 'flight details' or human_text == 'i want to know my flight details' or  human_text == 'which is my boarding gate' or  human_text =='what is my flight arrival time' or  human_text =='what is my flight departure time':
            print("ChatterBox:give me your flight information")
        else:
            if generate_greeting_response(human_text) != None:
                print("ChatterBox: " + generate_greeting_response(human_text))
            else:
                print("ChatterBox: ", end="")
                print(generate_response(human_text))
                article_sentences.remove(human_text)
                  
                if  human_text == 'Delta airlines Dl3' or human_text == 'HYC15' or human_text == 'Airbus 344':
                    print("ChatterBox:your flight will arrive at 8:30" )
                else:
                    if generate_greeting_response(human_text) != None:
                       print("ChatterBox: " + generate_greeting_response(human_text))
                    else:
                       print("ChatterBox:", end="")
                       print(generate_response(human_text))
                       article_sentences.remove(human_text)
                 
                       if human_text == 'thanks' or human_text == 'thank you very much' or human_text == 'thank you':
                            print("ChatterBox: Most welcome")
                       else:
                            if generate_greeting_response(human_text) != None:
                               print("ChatterBox: " + generate_greeting_response(human_text))
                            else:
                               print("ChatterBox: ", end="")
                               print(generate_response(human_text))
                               article_sentences.remove(human_text)
    else:
        continue_dialogue = False
        print("ChatterBox: Good bye and take care of yourself...")


while(continue_dialogue == True):
    human_text = input()
    human_text = human_text.lower()
    if human_text != 'bye':
        if human_text == 'i want to buy accessories' or human_text == 'i want to buy watch' or human_text == 'i want to buy gifts' or human_text == 'where can i find perfumes' or  human_text == 'where can i get toys' or  human_text =='gift shop' :
            print("ChatterBox:you can get watches from JUST IN VOOGUE")
        else:
            if generate_greeting_response(human_text) != None:
                print("ChatterBox: " + generate_greeting_response(human_text))
            else:
                print("ChatterBox: ", end="")
                print(generate_response(human_text))
                article_sentences.remove(human_text)
                  
                if human_text == 'thanks' or human_text == 'thank you very much' or human_text == 'thank you':
                   print("ChatterBox: Most welcome")
                else:
                   if generate_greeting_response(human_text) != None:
                      print("ChatterBox: " + generate_greeting_response(human_text))
                   else:
                      print("ChatterBox: ", end="")
                      print(generate_response(human_text))
                      article_sentences.remove(human_text)
    else:
        continue_dialogue = False
        print("ChatterBox: Good bye and take care of yourself...")