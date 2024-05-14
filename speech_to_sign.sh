#!/usr/bin/env bash

. ~/.bashrc

if (( $# != 1 ))
then
    echo "Usage: speech_to_sign.sh URL_OF_AUDIO"
fi

conda activate signgen

text="$(python speech_to_text.py "$1")"
echo "Text: $text"

#conda deactivate; conda activate texttospeech

gloss="$(python text_to_gloss.py "$text")"
echo "Gloss: $gloss"

python gloss_to_video.py "$gloss"

filename="out.mp4"

echo "File: $filename"

# echo ffmpeg -hide_banner -loglevel error -y -i "$filename" -vf "drawtext=fontfile=/usr/share/fonts/TTF/Roboto[wdth,wght].ttf:text='$gloss':fontcolor=white:fontsize=24:box=1:boxcolor=black@0.5:boxborderw=5:x=(w-text_w)/2:y=(h-text_h)/2" signwithtext.mp4
gloss_format="'$(printf '%q (%q)' "$text" "$gloss")'"
ffmpeg -y -hide_banner -loglevel error -i "$filename" -vf "drawtext=fontfile='/usr/share/fonts/TTF/Roboto[wdth,wght].ttf':text=$gloss_format:fontcolor=white:fontsize=24:box=1:boxcolor=black@0.5:boxborderw=5:x=(w-text_w)/2:y=(h-text_h)-40" signwithtext.mp4

echo "Added text"
