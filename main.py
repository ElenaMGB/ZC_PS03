# ///////////PS03
# ///////////Игра "Угадай слово по описанию"////////////////
# ///////////(слово подбирается случайно на сайте "RandomWord")////////////////

#Создаём функцию, которая будет получать информацию
from bs4 import BeautifulSoup
import requests

# Из-за нестабильной работы библиотеки  googletrans из-за изменений в API Google Translate применен
# альтернативный подход с использованием библиотеки deep_translator, которая обычно более стабильна.
# pip install deep_translator

# from googletrans import Translator - отключено

from deep_translator import GoogleTranslator

def get_russian_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
              
        word_div = soup.find("div", id="random_word")
        definition_div = soup.find("div", id="random_word_definition")
        
        if not word_div or not definition_div:
            print("Не удалось найти слово или определение на странице.")
            return None
        
        english_words = word_div.text.strip()
        word_definition = definition_div.text.strip()

        if not english_words or not word_definition:
            print("Получены пустые данные для слова или определения.")
            return None
        
        translator = GoogleTranslator(source='en', target='ru')
        try:
            russian_words = translator.translate(english_words)
            russian_definition = translator.translate(word_definition)
            
        except Exception as e:
            print(f"Ошибка при переводе: {e}")
            return None
        
        return {
            "english_words": english_words,
            "word_definition": word_definition,
            "russian_words": russian_words,
            "russian_definition": russian_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_russian_words()
        if word_dict is None:
            print("Не удалось получить слово. Попробуем еще раз.")
            continue

        english_words = word_dict["english_words"]
        russian_words = word_dict["russian_words"]
        word_definition = word_dict["word_definition"]
        russian_definition = word_dict["russian_definition"]

        print(f"Значение слова - {russian_definition} （{word_definition})")
        user = input(f"Что это за слово? ")
        if user.lower() == russian_words.lower():        
            print(f"Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {russian_words} （{english_words}）")

        play_again = input("Хотите сыграть еще раз? да/нет ")
        if play_again.lower() != "да":
            print("Спасибо за игру!")
            break

word_game()
