"""
    2019年 06月 11日 星期二 13:54:54 CST
"""
import requests


class HTTP:

    @staticmethod
    def get(url, returned_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if returned_json else ''
        return r.json() if returned_json else r.text
