import os
from pprint import pprint

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    def __init__(self):
        pass

    def process(self, data, inputs, utils):
        data = {}
        captions = {}
        for caption_file in os.listdir(CAPTIONS_DIR):
            time = None
            caption = None
            time_line = False
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                for line in f:
                    if '-->' in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        caption = line.strip()
                        captions[caption] = time
                        recorder_value = False
                data[caption_file] = captions
            pprint(data)
        return data
