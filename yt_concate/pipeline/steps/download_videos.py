from pytube import YouTube

from yt_concate.settings import VIDEOS_DIR
from yt_concate.pipeline.steps.step import Step


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print('videos to download=', len(yt_set))
        for yt in yt_set:
            if utils.check_video_file_exists(yt):
                print(yt.caption_id + '.mp4 file exists!!!!')
                continue
            try:
                print('downloading', yt.url)
                YouTube(yt.url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.caption_id + '.mp4')
            except Exception as e:
                print('download video error!!!', e)
                continue
        return data

