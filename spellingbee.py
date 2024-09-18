from gtts import gTTS
import os
import pygame

# Text to convert to speech
text_to_convert = 'Hey this is a spelling bee'

try:
    # Create a gTTS object
    tts = gTTS(text=text_to_convert, lang='en')

    # Specify output file path including filename
    output_file_path = r'D:\spelling_bee\audio.mp3'  # Ensure this path is correct
    
    # Save the audio to a temporary MP3 file
    tts.save(output_file_path)

    # Initialize the pygame mixer
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load(output_file_path)

    # Play the audio
    pygame.mixer.music.play()

    # Wait until the audio finishes playing
    while pygame.mixer.music.get_busy():
        continue

    print("Audio has been played successfully.")

except PermissionError as e:
    print(f"PermissionError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")