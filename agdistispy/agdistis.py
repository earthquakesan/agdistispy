import requests
import copy

class Agdistis(object):
    agdistisApi = 'http://akswnc9.informatik.uni-leipzig.de:8113/AGDISTIS'
    defaultAgdistisParams = {
                'text': '<entity>Leipzig</entity> is the capital of the world!',
                'type': 'agdistis'
                }

    def __init__(self):
        pass

    def disambiguate(self, text):
        """
            Input: text (any arbitrary string with annotated entities -- <entity>Austria</entity>)
            Output: entities as a list [{'start': 0, 'offset': 7, 'disambiguatedURL': 'http://dbpedia.org/resource/Austria', 'namedEntity': 'Austria'}]
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

    def disambiguateEntity(self, entity):
        """
            Support method to wrap entity into <entity/> tag
        """
        return self.disambiguate("<entity>%s</entity>"%(entity,))

if __name__ == "__main__":
    agdistis = Agdistis()
    entities = agdistis.disambiguate('<entity>Austria</entity>')
    entities = agdistis.disambiguateEntity('Austria')
    print(entities)
