from robot.api.deco import keyword

class AnotherLibrary:
    """Thrilling class"""

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self):
        self.i = 1

    @keyword('Call some function')
    def some_function(self):
        """Thrilling function

        Does it works? Let's see...
        """
        result = self.i * 'It works!! '
        self.i += 1
        return result
