from datetime import datetime
from gtts import gTTS
import os
import speech_recognition as sr
import time
from word2number import w2n

recognizer = sr.Recognizer()

current_datetime = datetime.now()
current_year = current_datetime.year
current_month = current_datetime.month
current_day = current_datetime.day

# Question identifiers
weight_question = "weight"
run_question = "run"
code_question = "code"
journal_question = "journal"
goodbye = "goodbye"


def create_statement(date, weight, run, code, journal):
    entry = (f"""
Date: {date} | Weight: {weight} kgs
Run: {run} kms | Code: {code} hrs

Journal Entry:
{journal}

------------------------------------------------------------
""")
    with open("records.txt", "a") as records:
        records.write(entry)


def make_audio_file(myText, audio_category):
    language = "en"
    myObj = gTTS(text=myText, lang=language, slow=False)
    myObj.save(f"audio/{audio_category}.mp3")


def listen():
    global recognizer
    run = True
    text = ""
    while run:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio).lower()
                print(f"Recognized: {text}")
                if text == "quit":
                    run = False
                    break
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            continue

        with open("output.txt", "w") as f:
            f.write(text)
        run = False
    return text


def format_date_for_yesterday(date_obj):
    date_obj_str = str(date_obj)
    day_part = int(date_obj_str[8:10])
    month_part = int(date_obj_str[5:7])
    if current_month > 1:
        if current_day == 1:
            day_part = 31
            month_part -= 1
        else:
            day_part -= 1
    return f"{current_year}/{month_part}/{day_part}"


def get_date():
    res_day = ""
    current_date = current_datetime.date()
    with open("output.txt", "r") as f:
        response = f.read()
    if "yesterday" in response or "no" in response:
        res_day = "yesterday"
        chosen_date = format_date_for_yesterday(current_date)
    else:
        res_day = "today"  # Default to today if no clear response
        chosen_date = current_date
    if res_day == "yesterday":
        date_text = f"Okay, so how much did you weigh yesterday?"
    else:
        date_text = f"Okay, so how much did you weigh today?"
    return date_text, chosen_date


def get_weight():
    with open("output.txt", "r") as f:
        weight = f.read().strip().replace("kilograms", "").replace("kg", "").strip()
    weight_text = f"{weight} kilograms. How much did you run?"
    if weight.isdigit():
        number = weight
    elif isinstance(weight, str):
        number = w2n.word_to_num(weight)
    else:
        number = weight_text
    return weight_text, number


def get_run():
    with open("output.txt", "r") as f:
        run = f.read().strip().replace("kilometers", "").replace("kilometer", "").replace("km", "").strip()
        if any(word in run for word in ["no", "didn't", "nothing", "none", "nup", "nope"]):
            run = "0"
    run_text = f"{run} kilometers. And coding?"
    if run.isdigit():
        number = run
    elif isinstance(run, str):
        number = w2n.word_to_num(run)
    else:
        number = run_text
    return run_text, number


def get_code():
    with open("output.txt", "r") as f:
        code = f.read().strip().lower().replace("hours", "").replace("hour", "").strip()
        if any(word in code for word in ["no", "didn't", "nothing", "none", "nup", "nope"]):
            code = "0"
    code_text = f"{code} hours. Would you like to make a journal entry?"
    if code.isdigit():
        number = code
    elif isinstance(code, str):
        number = w2n.word_to_num(code)
    else:
        number = code_text
    return code_text, number


def get_journal():
    with open("output.txt", "r") as f:
        journal = f.read().strip()
    journal_text = "Got it. Well, goodnight"
    return journal_text, journal


def get_yes_or_no():
    with open("output.txt", "r") as f:
        response = f.read().lower()
    return any(word in response for word in ["yes", "yep", "yeah", "sure", "please", "ok", "certainly"])


def main():
    journal_entry = ""

    os.system("start audio/welcome.mp3")
    listen()

    date_text, chosen_date = get_date()
    make_audio_file(date_text, weight_question)
    os.system("start audio/weight.mp3")
    time.sleep(1)
    listen()

    weight_text, weight_number = get_weight()
    make_audio_file(weight_text, run_question)
    os.system("start audio/run.mp3")
    time.sleep(1)
    listen()

    run_text, run_number = get_run()
    make_audio_file(run_text, code_question)
    os.system("start audio/code.mp3")
    time.sleep(1)
    listen()

    code_text, code_number = get_code()
    make_audio_file(code_text, journal_question)
    os.system("start audio/journal.mp3")
    time.sleep(2)
    listen()

    if get_yes_or_no():
        os.system("start audio/okay.mp3")
        time.sleep(1)
        listen()
        journal_text, journal_entry = get_journal()
        make_audio_file(journal_text, goodbye)
        os.system("start audio/bye.mp3")
    else:
        os.system("start audio/bye.mp3")

    create_statement(chosen_date, weight_number, run_number, code_number, journal_entry)


if __name__ == "__main__":
    main()
