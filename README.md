# Interactive Spelling Bee

A Python-based interactive spelling bee game that tests your spelling skills by playing audio pronunciations of random words and asking you to type them correctly.

## Features
- Fetches random words dynamically using the [Random Word API](https://random-word-api.herokuapp.com/).
- Retrieves definitions for the words using the [Free Dictionary API](https://dictionaryapi.dev/).
- Uses Google Text-to-Speech (`gTTS`) to generate audio pronunciations of the word and its definition.
- Plays the audio automatically using `pygame`.
- Tracks your score based on correct spellings.

## Prerequisites
- Python 3.x
- Required Python packages:
  - `gTTS`
  - `pygame`
  - `requests`

## Installation
1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install gTTS pygame requests
   ```
3. **Note:** The script currently saves audio files to a hardcoded directory `D:/spelling_bee`. Ensure this directory structure exists or update the `output_dir` variable in `spellingbee.py` to a valid path on your system.

## How to Play
1. Run the script:
   ```bash
   python spellingbee.py
   ```
2. Press Enter to start the game.
3. Listen to the audio playing the word and its definition. The definition will also be printed in the console.
4. Type your answer and press Enter.
5. The game will tell you if you are correct or incorrect and display your running total score.
6. Press Enter to proceed to the next word, or type `exit` to quit the game.
