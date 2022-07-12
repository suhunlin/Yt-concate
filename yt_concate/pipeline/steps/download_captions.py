import os

from pytube import YouTube

from .step import Step
from yt_concate.utils import Utils
from yt_concate.settings import CAPTIONS_DIR


class DownloadCaptions(Step):
    def __init__(self):
        print('DownloadCaptions was born!!!')

    def process(self, data, inputs, utils):
        for yt in data:
            if utils.caption_file_exists(yt):
                print('found existing caption file!!!')
                continue

            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError) as e:
                continue

            text_file = open(yt.caption_filepath, "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        return data
