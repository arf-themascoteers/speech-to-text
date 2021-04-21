import numpy as np

class GreedyOptimiser:
    def __init__(self, scores):
        self.scores = scores.copy()
        self.indexes = [None] * scores.shape[0]
        self.available_transcripts = list(range(scores.shape[1]))

    def optimize(self):
        while not self.is_done():
            max_score = -1
            max_student_index = -1
            max_transcript_index = -1
            for student_index, transcript_scores in enumerate(self.scores):
                if self.indexes[student_index] is None:
                    max_index = np.argmax(transcript_scores)
                    if transcript_scores[max_index] > max_score:
                        max_score = transcript_scores[max_index]
                        max_student_index = student_index
                        max_transcript_index = max_index

            if max_student_index != -1 and max_transcript_index != -1:
                self.indexes[max_student_index] = max_transcript_index
                self.scores[:,max_transcript_index] = -1
                self.scores[max_student_index,:] = -1

        return self.indexes

    def is_done(self):
        return None not in self.indexes

scores = np.array([[30,70,10],
                   [40,60,90]])
gd = GreedyOptimiser(scores)
gd.optimize()
print(gd.indexes)