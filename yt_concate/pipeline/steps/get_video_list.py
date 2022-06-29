import urllib.request
import json
import os

from yt_concate.pipeline.steps.step import Step


class GetVideoList(Step):

    def __init__(self):
        print('GetVideoList was born!!!')

    def process(self, data, inputs, utils):

        api_key = os.getenv('API_KEY')
        channel_id = inputs['channel_id']

        if utils.video_file_list_exists(channel_id):
            print('Found existing video list file for channel id!!!')
            return self.read_file(utils.get_video_list_filepath(channel_id))

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                            channel_id)

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)
            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break
        print(video_links)
        self.write_to_file(video_links, utils.get_video_list_filepath(channel_id))
        return video_links

    def write_to_file(self, video_links, filepath):
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                for url in video_links:
                    f.write(url + '\n')
        except Exception as e:
            print(e)

    def read_file(self, filepath):
        video_links = []
        try:
            with open(filepath, 'r') as f:
                for url in f:
                    video_links.append(url.strip())
        except Exception as e:
            print(__name__, 'read_file_error', e)

        return video_links


class StepException(Exception):
    pass
