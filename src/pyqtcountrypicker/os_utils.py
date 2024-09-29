import os


class OSUtils:

    @staticmethod
    def get_current_directory() -> str:
        """Get the current directory path

        :return: directory path
        """

        return os.path.dirname(os.path.realpath(__file__))
