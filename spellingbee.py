from gtts import gTTS
import os
import pygame
import requests

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

# Main function to handle the game loop
def play_game():
    while True:
        # Fetch a random word
        random_word = fetch_random_word()
        
        if random_word:
            print(f"Random word: {random_word}")

            # Get the definition of the random word
            definition = get_word_definition(random_word)

            # Check if a valid definition was returned
            if definition == "Definition not found.":
                print("No definition found. Selecting another word.")
                continue

            print("The definition of the word is: " + definition)

            # Prepare text for conversion to speech
            text_to_convert = f"{random_word}. {definition}"

            try:
                # Convert text to speech
                tts = gTTS(text=text_to_convert, lang='en')
                
                output_file_path = r'D:/spelling_bee/audio.mp3'  # Ensure this path is correct
                
                # Save the audio to a temporary MP3 file
                tts.save(output_file_path)

                # Initialize the pygame mixer
                pygame.mixer.init()

                # Load and play the audio file
                pygame.mixer.music.load(output_file_path)
                pygame.mixer.music.play()

                # Wait until the audio finishes playing
                while pygame.mixer.music.get_busy():
                    continue

                print("Press Enter to go to the next word.")
                input()  # Wait for the user to press Enter

            except PermissionError as e:
                print(f"PermissionError: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Could not retrieve a random word.")
            break

# Start the game
play_game()