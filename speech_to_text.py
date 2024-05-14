#!/usr/bin/env python3

import sys
import subprocess
import speech_recognition as sr
from urllib.request import urlretrieve


def speech_to_text(path):
    if "http://" in path or "https://" in path:
        # print("url downloading")
        filename = "input.ogg"
        urlretrieve(path, filename)
    else:
        filename = path
    try:
        subprocess.run(
            [
                "ffmpeg",
                "-hide_banner",
                "-loglevel",
                "error",
                "-y",
                "-i",
                path,
                "speech.wav",
            ],
            check=True,
        )
    except:
        pass

    r = sr.Recognizer()
    with sr.AudioFile("speech.wav") as source:
        audio = r.record(source)
    text = r.recognize_google(audio)
    return text


def main():
    print(speech_to_text(sys.argv[1]))


if __name__ == "__main__":
    main()
