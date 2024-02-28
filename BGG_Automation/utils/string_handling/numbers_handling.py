class NumbersHandling:
    @staticmethod
    def filter_digits(string):
        num = ''
        for char in string:
            if char.isdigit():
                num += char
        return int(num)
