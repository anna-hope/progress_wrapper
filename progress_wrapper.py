# (c) Anton Melnikov 2016

class ProgressWrapper:
    """
    Wraps an iterable and returns an iterable which acts like
    the original iterable and updates the given progress bar
    in the process.
    """

    def __init__(self, iterable, progressbar, total=None):
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
