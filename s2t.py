from google.cloud import speech


class Speech2Text:
    def __init__(self):

        # Instantiates a client
        client = speech.SpeechClient()

        # The name of the audio file to transcribe
        gcs_uri = "gs://gradclip1-audio/small.flac"

        audio = speech.RecognitionAudio(uri=gcs_uri)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
            language_code="en-AU",
            audio_channel_count = 2,
            enable_word_time_offsets = True
        )

        # Detects speech in the audio file
        operation = client.long_running_recognize(config=config, audio=audio)
        print("Waiting for operation to complete...")
        response = operation.result(timeout=9000)
        for result in response.results:
            for word in result.alternatives[0].words:
                start_time = word.start_time.microseconds
                end_time = word.end_time.microseconds
                #print(f"{result.alternatives[0].transcript},{result.alternatives[0].confidence},{word.word},{start_time},{end_time}")


