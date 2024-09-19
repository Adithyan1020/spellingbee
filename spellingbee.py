from gtts import gTTS
import os
import pygame
import requests
import datetime

# Function to get a random word
def fetch_random_word():
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()[0]
    else:
        print("Failed to fetch random word.")
        return None

# Function to get the definition of the random word
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

# Main function to handle the game loop
def play_game():
    # Initialize pygame mixer
    pygame.mixer.init()

    # Ensure the output directory exists
    output_dir = 'D:/spelling_bee'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    while True:
        # Fetch a random word
        random_word = fetch_random_word()
        
        if random_word:
            # Ask for help with definition or answer
            help_input = input("To ask for definition of the word, type 'd' or press 'a' to give answer: ")

            # Get the definition of the random word if requested
            definition = ""
            if help_input.lower() == 'd':
                definition = get_word_definition(random_word)
                print("The definition of the word is: " + definition)

            # Prepare text for conversion to speech
            text_to_convert = f"{random_word}. {definition}" if help_input.lower() == 'd' else f"{random_word}"

            try:
                # Convert text to speech
                tts = gTTS(text=text_to_convert, lang='en')
                
                # Generate a unique filename using timestamp
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                output_file_path = os.path.join(output_dir, f'audio_{timestamp}.mp3')  # Unique filename
                
                # Save the audio to a temporary MP3 file
                tts.save(output_file_path)

                # Load and play the audio file
                pygame.mixer.music.load(output_file_path)
                pygame.mixer.music.play()

                # Wait until the audio finishes playing
                while pygame.mixer.music.get_busy():
                    continue

                # Ask for user's answer after playing audio if they did not request a definition
                if help_input.lower() == 'a':
                    answer = input("Type your answer: ")
                    if answer.lower() == random_word.lower():
                        print("Your answer is correct!")
                    elif answer.lower()=='d':
                        definition = get_word_definition(random_word)
                        print("The definition of the word is: " + definition)

                    else:
                        print(f"You got it incorrect. The correct word was '{random_word}'.")

                print("Press Enter to go to the next word or type 'exit' to quit.")
                
                user_input = input()  # Wait for user input
                
                if user_input.lower() == 'exit':
                    print("Exiting the game. Thank you for playing!")
                    break  # Exit loop if user types 'exit'

            except PermissionError as e:
                print(f"PermissionError: {e}. Please ensure that the audio file is not open elsewhere.")
            except pygame.error as e:
                print(f"Pygame error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        
        else:
            print("Could not retrieve a random word.")
            break

# Start the game
play_game()