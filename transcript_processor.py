from transcript_info import TranscriptInfo
from word import Word


class TranscriptProcessor:
    def __init__(self):
        self.TRANSCRIPT_INFO = """
airing on is Daniel fish,0.7957906723022461,airing,0,400000
airing on is Daniel fish,0.7957906723022461,on,400000,700000
airing on is Daniel fish,0.7957906723022461,is,700000,0
airing on is Daniel fish,0.7957906723022461,Daniel,0,100000
airing on is Daniel fish,0.7957906723022461,fish,100000,400000
 QI howchin,0.4794796109199524,QI,600000,200000
 QI howchin,0.4794796109199524,howchin,200000,900000
 Mitchell dearing,0.7975555658340454,Mitchell,0,900000
 Mitchell dearing,0.7975555658340454,dearing,900000,300000
 Emily good,0.8179593086242676,Emily,0,600000
 Emily good,0.8179593086242676,good,600000,900000
 Bradley huggett,0.8221690654754639,Bradley,200000,200000
 Bradley huggett,0.8221690654754639,huggett,200000,500000
 Bailey Jensen,0.8702057600021362,Bailey,300000,300000
 Bailey Jensen,0.8702057600021362,Jensen,300000,100000
 Amy Marie Lange,0.6637791991233826,Amy,800000,400000
 Amy Marie Lange,0.6637791991233826,Marie,400000,800000
 Amy Marie Lange,0.6637791991233826,Lange,800000,100000
 Nicholas Moore,0.9325255155563354,Nicholas,0,900000
 Nicholas Moore,0.9325255155563354,Moore,900000,100000
 Reagan Paris,0.8336253762245178,Reagan,100000,0
 Reagan Paris,0.8336253762245178,Paris,0,400000
 James Piggott,0.844569206237793,James,0,800000
 James Piggott,0.844569206237793,Piggott,800000,200000
 Cody shot,0.48824015259742737,Cody,700000,500000
 Cody shot,0.48824015259742737,shot,500000,900000
 Jordan sins,0.7713832855224609,Jordan,200000,100000
 Jordan sins,0.7713832855224609,sins,100000,600000
 Blake Stone,0.9564103484153748,Blake,200000,200000
 Blake Stone,0.9564103484153748,Stone,200000,500000
 Esther Thompson,0.9102196097373962,Esther,100000,900000
 Esther Thompson,0.9102196097373962,Thompson,900000,500000
 Bachelor of civil engineering,0.9564103484153748,Bachelor,100000,300000
 Bachelor of civil engineering,0.9564103484153748,of,300000,300000
 Bachelor of civil engineering,0.9564103484153748,civil,300000,500000
 Bachelor of civil engineering,0.9564103484153748,engineering,500000,100000
"""
        self.TRANSCRIPT_INFO = self.TRANSCRIPT_INFO.strip()
        self.transcripts = []

    def process(self):
        transcript = None
        for line in self.TRANSCRIPT_INFO.splitlines():
            line = line.strip()
            tokens = line.split(",")
            name = tokens[0].strip().lower()
            if transcript == None or transcript.name != name:
                transcript = TranscriptInfo(name, tokens[1].strip())
                self.transcripts.append(transcript)
            word = Word(tokens[2].strip(), tokens[3].strip(), tokens[4].strip())
            transcript.words.append(word)

        return self.transcripts
