from bs4 import BeautifulSoup
import requests
import pprint

# PS03
# ///////////ПАРСИНГ ЦИТАТ2+game////////////////
#Создаём функцию, которая будет получать информацию

from googletrans import Translator

def get_russian_words():
    url = "https://randomword.com/russian"
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        russian_words = soup.find("div", id="random_word").text.strip()
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        translator = Translator()
        # russian_words = soup.find("div", id="random_word").text.strip()
        # word_definition = soup.find("div", id="random_word_definition").text.strip()
        russian_words = translator.translate(english_words, dest='ru').text
        russian_definition = translator.translate(word_definition, dest='ru').text
        return {
            "english_words": english_words,
            "word_definition": word_definition,
            "russian_words": russian_words,
            "word_definition": word_definition
            "russian_definition": russian_definition
        }
    except:
        print("Произошла ошибка")

# def get_english_words():
#    url = "https://randomword.com/"
#    try:
#        response = requests.get(url)
# #Создаём объект Soup
#        soup = BeautifulSoup(response.content, "html.parser")
# #Получаем слово. text.strip удаляет все пробелы из результата
#        english_words = soup.find("div", id="random_word").text.strip()
# #Получаем описание слова
#        word_definition = soup.find("div", id="random_word_definition").text.strip()
#        #переводим
#        translator = Translator()
#        russian_words = translator.translate(english_words, dest='ru').text
# #Чтобы программа возвращала словарь
#        return {
#            "english_words": english_words,
#            "word_definition": word_definition,
#            "russian_words": russian_words
#        }
#    #Функция, которая сообщит об ошибке, но не остановит программу
#    except:
#        print("Произошла ошибка")


def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_russian_words()
        russian_words = word_dict.get("russian_words")
        word_definition = word_dict.get("word_definition")
        word_definition = word_dict.get("russian_definition")

        print(f"Значение слова - {word_definition}")
        user = input(f"Что это за слово? ")
        if user == russian_words:
            print(f"Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {russian_words}")

        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break

# Создаём функцию, которая будет делать саму игру
# def word_game():
#     print("Добро пожаловать в игру")
#     while True:
#         # Создаём функцию, чтобы использовать результат функции-словаря
#         word_dict = get_english_words()
#         word = word_dict.get("english_words")
#         word_definition = word_dict.get("word_definition")
#
#         russian_words = word_dict.get("russian_words")
#         print(f"Значение слова - {word_definition}")
