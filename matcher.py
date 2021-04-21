from csv_processor import CSVImporter
from transcript_processor import TranscriptProcessor
import random
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class Matcher:
    def __init__(self, students, transcripts):
        self.students = students
        self.transcripts = transcripts
        self.indexes = list(range(len(students)))
        self.discard = {"bachelor", "philosophy", "engineering"}

    def print(self):
        print(f"Count Students: {len(self.students)}")
        print(f"Count Transcripts: {len(self.transcripts)}")
        print("Students")
        print("========")
        for student in self.students:
            print(student.name)
        print("Transcripts")
        print("========")
        for transcript in self.transcripts:
            print(transcript.name)

    def match(self):
        if(len(self.transcripts) > len(self.students)):
            self.discard_names()

        for student_index, student in enumerate(self.students):
            max_score = -1
            max_score_index = -1
            for transcript_index, transcript in enumerate(self.transcripts):
                if not self.taken(student_index, transcript_index):
                    score = fuzz.ratio(student.name, transcript.name)
                    if score > max_score:
                        max_score = score
                        max_score_index = transcript_index

            self.indexes[student_index] = max_score_index

    def taken(self, before_student_index, transcript_index):
        if before_student_index == 0:
            return False
        for i in range(before_student_index):
            if self.indexes[i] == transcript_index:
                return True
        return False

    def discard_names(self):
        new_transcripts = []
        for transcript in self.transcripts:
            should_discard = False
            for word in transcript.words:
                if word.word in self.discard:
                    should_discard = True
                    break
            if not should_discard:
                new_transcripts.append(transcript)

        self.transcripts = new_transcripts

    def print_match(self):
        for i,j in enumerate(self.indexes):
            print(f"{self.students[i].name} = {self.transcripts[j].name}")


cp = CSVImporter()
students = cp.process()

tp = TranscriptProcessor()
transcripts = tp.process()
random.shuffle(transcripts)
matcher = Matcher(students, transcripts)
matcher.discard_names()
matcher.print()
print("Before Match")
print("============")
matcher.print_match()
matcher.match()
print("After Match")
print("============")
matcher.print_match()
