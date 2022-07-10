import os

from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import VIDEOS_DIR


class YT:
    def __init__(self, url):
        self.url = url
        self.caption_id = self.get_caption_id_from_url()
        self.caption_filepath = self.get_caption_file_path()
        self.video_filepath = self.get_video_file_path()
        self.captions = {}

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    def get_caption_id_from_url(self):
        return self.url.split('watch?v=')[-1]

    def get_caption_file_path(self):
        return os.path.join(CAPTIONS_DIR, self.caption_id + '.txt')

    def get_video_file_path(self):
        return os.path.join(VIDEOS_DIR, self.caption_id + '.mp4')

    def __str__(self):
        return '<yt :' + self.caption_id + '>'

    def __repr__(self):
        content = ':'.join([
            'caption id :' + self.caption_id,
            'caption file path:' + self.caption_filepath,
        ])
        return '<YT information:' + content + '>'
