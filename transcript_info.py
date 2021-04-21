class TranscriptInfo:
    def __init__(self, name, confidence):
        self.name = name
        self.confidence = confidence
        self.words = []

    def __str__(self):
        return f"{self.name} {self.confidence}\nWORDS:\n{self.words}"

    def __repr__(self):
        return "\n" + self.__str__() + "\n"