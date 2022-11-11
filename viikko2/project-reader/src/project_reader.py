from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        dict_toml = toml.loads(content, _dict=dict)
        dict_toml = dict_toml['tool']
        dict_toml = dict_toml['poetry']
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(dict_toml['name'], dict_toml['description'], dict_toml['dependencies'], dict_toml['dev-dependencies'])
