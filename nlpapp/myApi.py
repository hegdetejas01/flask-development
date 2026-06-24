import nlpcloud

class API:

    def __init__(self):
        self.apiKey = "e90e6e9ee98f28fae68de4e665577a9554dce624"

    def sentimentAnalysis(self, text):
        client = nlpcloud.Client("gpt-oss-120b", self.apiKey, gpu=True)
        response = client.sentiment(text, target="NLP Cloud")
        return response