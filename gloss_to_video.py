#!/usr/bin/env python3

import sys
import random
import os.path
import subprocess
from pathlib import Path


WORDS_DIR = Path("words")


def get_random_file(directory):
    """return random file from the given dir"""
    return str(directory / random.choice(os.listdir(directory)))


def gloss_to_video(gloss):
    args = gloss.upper()
    words = args.strip().split()
    print(words)

    image_files = []
    for word in words:
        # if word found, add to slideshow
        if os.path.exists(WORDS_DIR / word):
            # print(word, "found")
            image_files.append(get_random_file(WORDS_DIR / word))
        # else split word into letters and add each letter
        else:
            print(word, "not found. Splitting into letters")
            letters = list(word)
            for letter in letters:
                if os.path.exists(WORDS_DIR / letter):
                    # print(letter, "found")
                    image_files.append(get_random_file(WORDS_DIR / letter))
                else:
                    print("letter", letter, "not found")

    # print(image_files)

    with open("sequence.txt", "w", encoding="utf-8") as f:
        f.write("file '" + image_files[0] + "'\nduration 1\n")
        for image in image_files:
            f.write("file '" + image + "'\nduration 1\n")
        f.write("file '" + image_files[-1] + "'\n")

    ffmpeg_cmd = (
        "ffmpeg -y -hide_banner"
        + " -loglevel error -f concat -safe 0"
        + " -i sequence.txt"
        + " -filter_complex scale=w=1920:h=1080:force_original_aspect_ratio=1,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=25,format=yuv420p"
        + " -c:v libx264"
        + " out.mp4"
    ).split()

    # print(ffmpeg_cmd)
    subprocess.run(
        ffmpeg_cmd,
        check=True,
    )


if __name__ == "__main__":
    gloss_to_video(sys.argv[1])
