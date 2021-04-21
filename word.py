class Word:
    def __init__(self, word, start, end):
        self.word = word.lower()
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.word} {self.start} {self.end}"

    def __repr__(self):
        return "\n" + self.__str__() + "\n"