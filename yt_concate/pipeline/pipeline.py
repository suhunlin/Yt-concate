from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = ['https://www.youtube.com/watch?v=SeXZt5hqe6I',
                'https://www.youtube.com/watch?v=ML_isAjmxtw',
                'https://www.youtube.com/watch?v=QfKvT5J3ZSk',
                'https://www.youtube.com/watch?v=YAvhJNNQ2XQ',
                ]
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils)
            except StepException as e:
                print('Step error in ', step, e)
                break
