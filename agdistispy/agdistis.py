import requests
import copy

class Agdistis(object):
    agdistisApi = 'http://139.18.2.164:8080/AGDISTIS'
    defaultAgdistisParams = {
                'text': '<entity>Leipzig</entity> is the capital of the world!',
                'type': 'agdistis'
                }

    def __init__(self):
        pass

    def disambiguate(self, text):
        """
            Input: text (any arbitrary string with annotated entities -- <entity>Leipzig</entity>)
            Output: recognized entities packed in tuple (input, output, log)
        """
        payload = copy.copy(self.defaultAgdistisParams)
        payload['text'] = text
        r = requests.post(self.agdistisApi, data=payload)
        entities = []
        try:
            entities = r.json()
        except ValueError as e:
            #server failed
            entities = [{'start': 0, 'offset': 0, 'disambiguatedURL': '', 'namedEntity': ''}]
        return entities

if __name__ == "__main__":
    agdistis = Agdistis()
    entities = agdistis.disambiguate('<entity>Austria</entity>')
