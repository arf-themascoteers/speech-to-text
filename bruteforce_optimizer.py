class BruteForceOptimizer:
    def __init__(self, scores):
        self.scores = scores

    def optimize(self, pivot, after_indexes):
        if len(after_indexes) == 0:
            return 0,[]
        max_score = -1
        max_arrangements = []
        for transcript_index in after_indexes:
            copied = after_indexes.copy()
            copied.remove(transcript_index)
            my_score = self.scores[pivot][transcript_index]
            rest_score, arrangements = self.optimize(pivot+1,copied)
            if rest_score + my_score > max_score:
                max_score = rest_score + my_score
                max_arrangements = [transcript_index] + copied
        return max_score, max_arrangements
