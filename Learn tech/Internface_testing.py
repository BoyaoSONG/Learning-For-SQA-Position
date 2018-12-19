import unittest
import json
import requests

class Demo(unittest.TestCase):

    def test_jiekou(self):
        self.data = {'username': 'username', 'password': 'password'}
        self.r = requests.post('http://127.0.0.1:8000/polls/', data= self.data)
        self.data_get = self.r.text
        print(self.data_get)
        self.data_dic = json.loads(self.data_get)
        print(self.data_dic)
        self.trate_result(self.data_dic)

    def trate_result(self,result):
        print(result['list'][0]['0'])


if __name__ == "__main__":
    unittest.main()