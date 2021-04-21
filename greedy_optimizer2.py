import numpy as np

class GreedyOptimiser2:
    def __init__(self, scores):
        self.scores = scores.T
        self.max_index_array = [np.argmax(i) for i in self.scores]
        self.indexes = [-1] * self.scores.shape[1]

    def optimize(self):
        n_students = scores.shape[1]
        for student_index in range(n_students):
            indexes = np.argwhere(self.max_index_array == student_index)
            max_value = -1
            max_index = -1
            for transcript_index in indexes:
                if self.max_index_array[transcript_index][student_index] > max:
                    max_value = self.max_index_array[transcript_index][student_index]
                    max_index = transcript_index
            self.indexes[student_index] = max_index


scores = np.array([[30,70,10],
                   [40,60,90]])
gd = GreedyOptimiser2(scores)
gd.optimize()


