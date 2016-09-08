# A ProgressBar implementation for tqdm (https://github.com/tqdm/tqdm)
# (c) Anton Melnikov 2016

from tqdm import tqdm

from . import ProgressBar


class TqdmWrapper(ProgressBar):
    def __init__(self, total=0, tqdm_=None):
        if tqdm:
            self.tqdm = tqdm_
        else:
            self.tqdm = tqdm()

    @property
    def total(self):
        return self.tqdm.total

    @total.setter
    def total(self, total):
        self.tqdm.total = total

    def update_progress(self, n=1):
        self.tqdm.update(n)

    def reset(self):
        self.tqdm.clear()

    def set_progress(self, n=1):
        self.tqdm.clear()
        self.tqdm.update(n)
