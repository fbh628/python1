import sys


class ArgParser():
    def __init__(self):
        self.args = sys.argv

    def get(self):
        try:
            return self.args[1], self.args[2]
        except IndexError:
            return "default", ""
