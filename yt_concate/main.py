from utils import Utils
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.steps.preflight import Preflight

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Postflight(),
    ]
    # inputs = dict(channel_id = CHANNEL_ID)
    inputs = {
        'channel_id': CHANNEL_ID
    }
    utils = Utils()
    print(utils.caption_file_exists('https://www.youtube.com/watch?v=VZzTcukOwbs'))
    pipeline1 = Pipeline(steps)
    pipeline1.run(inputs, utils)


if __name__ == '__main__':
    main()
