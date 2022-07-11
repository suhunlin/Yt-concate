from yt_concate.utils import Utils
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos

def main():
    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),

    ]
    inputs = {
        'channel_id' : 'UCKSVUHI9rbbkXhvAXK-2uxA',
        'search_word': 'incredible',

    }
    utils = Utils()
    p1 = Pipeline(steps)
    p1.run(inputs, utils)



if __name__ == '__main__':
    main()
