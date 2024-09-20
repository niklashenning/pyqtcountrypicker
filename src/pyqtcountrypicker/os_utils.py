import os


class OSUtils:

    @staticmethod
    def get_current_directory() -> str:
        return os.path.dirname(os.path.realpath(__file__))
