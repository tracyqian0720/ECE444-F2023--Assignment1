# pylint: disable=no-self-argument
# pylint: disable=all
class Utils:

    def reversed(self, num: int) -> int:
        num = str(num)[::-1]
        return int(num)

    def formatter(self, num: int) -> tuple:
        binary = bin(num)
        octal = oct(num)
        return (binary, octal)

    
