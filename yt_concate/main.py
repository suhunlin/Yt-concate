from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.get_video_list import StepException
from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    steps = [
        GetVideoList(),
    ]
    # inputs = dict(channel_id = CHANNEL_ID)
    inputs = {
        'channel_id': CHANNEL_ID
    }
    pipeline1 = Pipeline(steps)
    pipeline1.run(inputs)


if __name__ == '__main__':
    main()
