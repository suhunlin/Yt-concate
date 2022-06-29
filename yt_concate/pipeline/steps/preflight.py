from yt_concate.pipeline.steps.step import Step

class Preflight(Step):
    def __init__(self):
        pass

    def process(self, data, inputs, utils):
        utils.create_dir()
