# Voice-Driven Daily Activity Logger

This project is a voice-driven daily activity logger that records daily metrics such as weight, running distance, coding time, and a journal entry using speech recognition. The program uses Google Text-to-Speech (gTTS) to provide voice prompts and SpeechRecognition to listen to and interpret user responses.

## Features

- Records daily activities: weight, running distance, coding time, and a journal entry.
- Voice prompts for questions using Google Text-to-Speech (gTTS).
- Speech recognition for capturing and processing user responses.
- Automatically saves the entries to a text file (`records.txt`).

## Requirements

- Python 3.6 or above
- Required Python packages:
  - `gTTS` (Google Text-to-Speech)
  - `SpeechRecognition`
  - `pyaudio`
  - `word2number`
  
## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sapporoalex/voice-driven-activity-logger.git
    cd voice-driven-activity-logger
    ```

2. Install the required packages:

    ```bash
    pip install gTTS SpeechRecognition pyaudio word2number
    ```

## Usage

1. Run the main script:

    ```bash
    python main.py
    ```

2. Follow the voice prompts and speak your responses. The program will ask for:

   - The date (today or yesterday).
   - Your weight in kilograms.
   - The distance you ran in kilometers.
   - The number of hours you spent coding.
   - Optionally, a journal entry.

3. The responses will be saved in `records.txt`.
<img src="https://github.com/SapporoAlex/Voice-Driven-Daily-Activity-Logger/blob/main/audio-driven-daily-activity-logger-example-output.jpg" alt="image of example output">
example output

## How It Works

1. **Voice Prompts:** The program uses Google Text-to-Speech (gTTS) to generate audio prompts for each question.
2. **Speech Recognition:** The user's responses are captured via the microphone and interpreted using Google's SpeechRecognition API.
3. **Data Logging:** The responses are processed, converted to numerical values where necessary, and saved to `records.txt`.

## File Structure

- `main.py`: Main script to run the program.
- `records.txt`: Text file where daily activity logs are stored.
- `audio/`: Directory containing generated audio files for prompts.

## Customization

- You can customize the prompts and add more questions by modifying the `self_checker_audio_input.py` file.
- To change the output format of the entries, modify the `create_statement()` function in `self_checker_audio_input.py`.

## Dependencies

- [gTTS](https://pypi.org/project/gTTS/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [PyAudio](https://pypi.org/project/PyAudio/)
- [word2number](https://pypi.org/project/word2number/)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or report an issue.

## Acknowledgments

- [Google Text-to-Speech (gTTS)](https://pypi.org/project/gTTS/) for audio prompts.
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for speech input.
- Python community for useful packages and resources.

## Author

- [SapporoAlex](https://github.com/yourusername)

