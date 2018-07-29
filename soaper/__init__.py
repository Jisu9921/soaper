import xml.etree.ElementTree as ET
from urllib import request, parse
from copy import copy


def soap_request(url, data):
    req = request.Request(url, data=data.encode('utf-8'),
                          headers={'content-type': 'text/xml;charset=utf-8'}, method='POST')
    rep = request.urlopen(req)
    return xml_to_dict(ET.fromstring(rep.read().decode('utf-8'))) if rep.getcode() is 200 else None


def url_decode(url):
    return parse.unquote(url)


def strip_tag_name(t):
    idx = t.rfind("}")
    if idx != -1:
        t = t[idx + 1:]
    return t


def xml_to_dict(r, root=True):
    if root:
        return {strip_tag_name(r.tag): xml_to_dict(r, False)}
    d = copy(r.attrib)
    if r.text:
        d['text'] = r.text
    for x in r.findall("./*"):
        if x.tag not in d:
            d[strip_tag_name(x.tag)] = []
        d[strip_tag_name(x.tag)].append(xml_to_dict(x, False))
    return d


