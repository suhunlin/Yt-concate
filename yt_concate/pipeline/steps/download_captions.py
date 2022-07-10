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
                language_code = 'a.en'
                full_filename = yt.get_caption_filepath()
                caption_file = self.get_caption(source, language_code)

            except (KeyError, AttributeError) as e:
                print(e, 'Error occur in url :', yt.url)
                continue
            self.save_to_text_file(full_filename, caption_file)
        return data

    def get_caption(self, source, language_code):
        en_caption = source.captions.get_by_language_code(language_code)
        # print(en_caption.xml_captions)
        en_caption_convert_to_srt = (en_caption.generate_srt_captions())
        # print(en_caption_convert_to_srt)
        return en_caption_convert_to_srt

    def save_to_text_file(self, full_filename, caption_file):
        # save the caption to a file named Output.txt
        text_file = open(full_filename, "w", encoding='utf-8')
        text_file.write(caption_file)
        text_file.close()
