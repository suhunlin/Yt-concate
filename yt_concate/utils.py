import os

from settings import DOWNLOADS_DIR
from settings import CAPTIONS_DIR
from settings import VIDEOS_DIR
from settings import SEPARATE_VIDEO_ID_BY


class Utils:
    def __init__(self):
        pass

    def create_dir(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)

    def caption_file_exists(self, url):
        path = self.get_caption_filepath(url)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_file_list_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path)

    @staticmethod
    def get_vedio_id_from_url(url):
        return url.split(SEPARATE_VIDEO_ID_BY)[-1]

    @staticmethod
    def get_caption_filepath(url):
        file_type = '.txt'
        return os.path.join(CAPTIONS_DIR, Utils.get_vedio_id_from_url(url) + file_type)
