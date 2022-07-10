from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None

        try:
            for step in self.steps:
                data = step.process(data, inputs, utils)
        except StepException as e:
            print(step,'error in ', e)
