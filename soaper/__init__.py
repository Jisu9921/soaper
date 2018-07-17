import requests
import xml.etree.ElementTree as ET
from urllib.parse import unquote
from copy import copy


class Response:
    def __init__(self):
        self.headers = {'content-type': 'text/xml;charset=utf-8'}

    def get(self, url, data):
        resp = requests.post(url=url, data=data, headers=self.headers)
        contents = resp.content.decode('utf-8')
        return resp.status_code, contents

    def get_dict(self, url, data):
        resp = self.get(url, data)
        return self.xml_to_dict(ET.fromstring(resp[1])) if resp[0] is 200 else resp

    def xml_to_dict(self, r, root=True):
        if root:
            return {self.strip_tag_name(r.tag): self.xml_to_dict(r, False)}
        d = copy(r.attrib)
        if r.text:
            d['text'] = r.text
        for x in r.findall("./*"):
            if x.tag not in d:
                d[self.strip_tag_name(x.tag)] = []
            d[self.strip_tag_name(x.tag)].append(self.xml_to_dict(x, False))
        return d

    @staticmethod
    def url_decode(data):
        return unquote(data)

    @staticmethod
    def strip_tag_name(t):
        idx = t.rfind("}")
        if idx != -1:
            t = t[idx + 1:]
        return t
