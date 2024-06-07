# Two goals with this test.py. First, being able to download mp3 file. Second, being able to crop the mp3 file. Third, massively crop mp3 files.
from bs4 import BeautifulSoup as bs
import xml.etree.ElementTree as ET
import requests

# import soundfile as sf
import pydub
# oh no no no,...
#import ffmpeg  

from pydub import AudioSegment
# This does not work for Mac system, don't know why. But it will be another debug session?
pydub.AudioSegment.converter = "[REPLACE WITH YOUR PATH]"


# Preparation: get the start and end from the xml file, maybe try beautiful soup??
def extract_by_tag(data_path: str):
    """Extract the data according to a given tag from the given data path. I decide to move the language tag recognition to later.

    Returns:
        list: an array contains all the sentences.
    """
    try:
        with open(data_path) as f:
            bs_data = bs(f.read(), "xml")
            tag_data = bs_data.find_all("S")
            total_start, total_end = [], []
            for each_td in tag_data:
                middle_process = each_td.find_all("AUDIO", recursive=False)
                total_start.extend(sentence.get("start") for sentence in middle_process)
                total_end.extend([sentence.get("end") for sentence in middle_process])
    except Exception as e:
        print(f"error is {e}")
    timestemp = {}
    idx = 0
    for s, e in zip(total_start, total_end):
        timestemp[idx] = [float(s), float(e)]
        idx += 1
    return timestemp


# First task.
def download_audio_from_link(link: str, data_dir: str, filename):
    r = requests.get(link)
    if r.status_code == 200:
        with open(f"{data_dir}/{filename}", "wb") as audio_file:
            audio_file.write(r.content)
        return f"{data_dir}/{filename}"
    else:
        return r.status_code


# Second task.
# It works!!!!!!!!!!!AHHHHHHHH
def clip_audio(input_file: str, start: float, end: float):
    audio_file = AudioSegment.from_file(input_file)
    seg = audio_file[start*1000:end*1000]
    seg.export("Data/test_clip_output.wav", format="wav")
    return


# Third task.


if __name__ == "__main__":
    # testing.
    # Preparation
    # test_result = extract_by_tag("Data/crdo-JYA_DELUGE.xml")
    # First task
    # test = download_audio_from_link("https://cocoon.huma-num.fr/data/archi/masters/125767.wav", "Data", "test.wav")

    # Second task
    test_clip = clip_audio("Data/test.wav", 7.5298, 12.0056)
