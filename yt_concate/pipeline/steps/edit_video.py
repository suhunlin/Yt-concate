from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips

from .step import Step


class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            if not utils.check_video_file_exists(found.yt):
                print(found.yt.caption_id + '.mp4 file not exists!!!')
                continue
            start, end = self.parse_caption_time(found.time)
            try:
                video = VideoFileClip(found.yt.video_filepath).subclip(10, 20)
                # video = VideoFileClip(found.yt.video_filepath).subclip(start, end)
            except ValueError as e:
                print('EditVideo error in ', e)
                continue
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break
        output_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile(output_filepath)

    def parse_caption_time(self, caption_time):
        start, end = caption_time.strip().split(' --> ')
        return self.parse_time_str(start), self.parse_time_str(end)

    def parse_time_str(self, time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms) / 1000
