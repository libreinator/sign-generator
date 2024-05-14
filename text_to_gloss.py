#!/usr/bin/env python3

"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import sys
import google.generativeai as genai
from secrets import API_KEY

genai.configure(api_key=API_KEY)

# Set up the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]


def text_to_gloss(input_text):
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-latest",
        generation_config=generation_config,
        safety_settings=safety_settings,
    )

    prompt_parts = [
        'You are a proficient assistant, responsible for data sanitization for a machine translation model. Your main task involves operating the normalize function:\n\n  Normalizes the given text for sign language translation and generate gloss in indian sign language. The output can be different from the input text as long as the words convey the same meaning.\n\n  Takes in a text that might contain misspellings, incorrect capitalization,\n  missing hyphenation, numbers, units, or other phenomena requiring special\n  vocalization. Returns the gloss normalized for indian sign language, with uppercase letters, all words separated by spaces.\n\n  Parameters:\n    - input_text (str): The text to be normalized.\n\n  Returns:\n    - str: The normalized gloss suitable for indian sign language.\nUse text from this list whenever possible: "ABUSE", "AFRAID", "AGREE", "ALL", "A_LOT", "ANGRY", "ANYTHING", "APPRECIATE", "BAD", "BEAUTIFUL", "BECOME", "BED", "BORED", "BRING", "CHAT", "CLASS", "COLD", "COLLEGE_SCHOOL", "COMB", "COME", "CONGRATULATIONS", "CRYING", "DARE", "DIFFERENCE", "DILEMMA", "DISAPPOINTED", "DO", "DONT_CARE", "ENJOY", "FAVOUR", "FEVER", "FINE", "FOOD", "FREE", "FRIEND", "FROM", "GO", "GOOD", "GRATEFUL", "HAD", "HAPPENED", "HAPPY", "HEAR", "HEART", "HELLO_HI", "HELP", "HIDING", "HOW", "HUNGRY", "HURT", "I_ME_MINE_MY", "KIND", "LEAVE", "LIKE", "LIKE_LOVE", "MEAN_IT", "MEDICINE", "MEET", "NAME", "NICE", "NOT", "NUMBER", "OLD_AGE", "ON_THE_WAY", "OUTSIDE", "PHONE", "PLACE", "PLEASE", "POUR", "PREPARE", "PROMISE", "REALLY", "REPEAT", "ROOM", "SERVE", "SHIRT", "SITTING", "SLEEP", "SLOWER", "SOFTLY", "SOME_HOW", "SOME_ONE", "SOMETHING", "SO_MUCH", "SORRY", "SPEAK", "STOP", "STUBBORN", "SURE", "TAKE_CARE", "TAKE_TIME", "TALK", "TELL", "THANK", "THAT", "THINGS", "THINK", "THIRSTY", "TIRED", "TODAY", "TRAIN", "TRUST", "TRUTH", "TURN_ON", "UNDERSTAND", "WANT", "WATER", "WEAR", "WELCOME", "WHAT", "WHERE", "WHO", "WORRY", "YOU"\nPlease reply with only the gloss as output, without escaping the underscores.\n\nINPUT: {}'.format(
            input_text
        ),
    ]

    response = model.generate_content(prompt_parts)
    return str(response.text)


if __name__ == "__main__":
    print(text_to_gloss(sys.argv[1]))
