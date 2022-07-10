from yt_concate.model.found import Found
from yt_concate.pipeline.steps.step import Step


class Search(Step):
    def process(self, data, inputs, utils):
        found = []
        search_word = inputs['search_word']
        for yt in data:
            captions = yt.captions
            if not captions:
                continue
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    found.append(Found(yt, caption, time))
        return found
