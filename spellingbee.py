from gtts import gTTS
import os
import pygame
import requests
import datetime

def fetch_random_word():
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()[0]
    else:
        print("Failed to fetch random word.")
        return None

def get_word_definition(random_word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{random_word}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        definitions = []
        
        for meaning in data[0]["meanings"]:
            for definition in meaning["definitions"]:
                definitions.append(definition["definition"])
        
        return ", ".join(definitions) if definitions else "Definition not found."
    else:
        return "Definition not found."

print("This is a spelling bee competition..")
input('Press Enter to start...')

def play_game():
    count = 0
    pygame.mixer.init()
    output_dir = 'D:/spelling_bee'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    while True:
        random_word = fetch_random_word()
        
        if random_word:
            definition = get_word_definition(random_word)
            print("The definition of the word is: " + definition)

            if definition == 'Definition not found.':
                continue

            text_to_convert = f"{random_word}. {definition}"

            try:
                tts = gTTS(text=text_to_convert, lang='en')
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                output_file_path = os.path.join(output_dir, f'audio_{timestamp}.mp3')
                tts.save(output_file_path)

                pygame.mixer.music.load(output_file_path)
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    continue

                answer = input("Type your answer: ")
                if answer.lower() == random_word.lower():
                    print("Your answer is correct!")
                    count += 1
                    
                else:
                    print(f"You got it incorrect. The correct word was '{random_word}'.")

                print("Press Enter to go to the next word or type 'exit' to quit.")
                
                user_input = input()
                
                if user_input.lower() == 'exit':
                    print("Exiting the game. Thank you for playing!")
                    break

            except PermissionError as e:
                print(f"PermissionError: {e}. Please ensure that the audio file is not open elsewhere.")
            except pygame.error as e:
                print(f"Pygame error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        
        else:
            print("Could not retrieve a random word.")
            break
        print(f"The total score is {count}")

play_game()