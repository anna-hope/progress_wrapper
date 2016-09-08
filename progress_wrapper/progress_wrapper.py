# (c) Anton Melnikov 2016

import abc

class ProgressBar(abc.ABC):
    def __iter__(self, total=0):
        ...

    @property
    @abc.abstractmethod
    def total(self):
        ...

    @total.setter
    @abc.abstractmethod
    def total(self, total):
        ...

    @abc.abstractmethod
    def update_progress(self, n=1):
        ...

    @abc.abstractmethod
    def reset(self):
        ...

    @abc.abstractmethod
    def set_progress(self, n=1):
        ...


class ProgressWrapper:
    """
    Wraps an iterable and returns an iterable which acts like
    the original iterable and updates the given progress bar
    in the process.
    """

    def __init__(self, iterable, progressbar: ProgressBar, total=None):
        """
        Parameters
        :param iterable: iterable
        :param progressbar:
            A progress bar object. It has to have an attribute "total"
            and a method "update_progress([n])"
        :param total: int
            The length of the iterabld
        """
        self.iterable = iterable
        self.progressbar = progressbar

        if total:
            self.total = total
        else:
            try:
                self.total = len(iterable)
            except TypeError:
                raise ValueError('Could not determine the length of the iterable, '
                                 + 'and no total was given.')

        self.progressbar.total = self.total


    def __iter__(self):
        for element in self.iterable:
            yield element
            self.progressbar.update_progress()

    def reset(self):
        self.progressbar.reset()



