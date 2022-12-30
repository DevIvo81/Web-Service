import os
import requests

from selectorlib import Extractor
from fake_useragent import UserAgent


class MakeYamlCall:

    def __init__(self, url, yaml_file):
        self.url = url
        self.yaml_file = yaml_file
        
        self.data = self.acquire_data()
    
    
    def acquire_data(self):
        """The function that parses yml file data from the given url
        and returns a dictionary of data.

        Args:
            url (str): path[str]
            yaml_file (str): path[str]

        Returns:
            dict: Dictionary of Selectorlib extracted website data
        """
        ua = UserAgent()
        headers = {"User-Agent" : ua.random}

        e = Extractor.from_yaml_file(f"{os.getcwd()}\\app\\static\\yaml\\{self.yaml_file}")

        r = requests.get(self.url, headers=headers)
        if r.status_code == 200:
            data = e.extract(r.text)
            return data
        else:
            return ("center><h1>Bad GET response!</h1></center>")











