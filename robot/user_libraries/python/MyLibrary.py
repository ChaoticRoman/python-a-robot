
class MyLibrary:
    """Some class documentation..."""

    def __init__(self, arg):
        self.arg = int(arg)
        print arg

    def get(self, message):
        """Returns some string..."""
        result = self.arg + 10
        print(result)
        return str(result)
