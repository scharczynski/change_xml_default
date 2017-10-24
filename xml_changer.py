import xml.etree.ElementTree as etree
import json
from pprint import pprint
import re


def change_element(file, tag, wire_name, attr_name, value, output_file=file):

    e = etree.parse(file)
    root = e.getroot()
    m = re.match('\{.*\}', root.tag).group(0)
    find_string = ".//" + m + tag + "[@name='" + wire_name + "']"
    node = root.findall(find_string)[0]
    node.set(attr_name, str(value))
    print node.get('scaleC')

    e.write(file)


def verify_change(file, tag, wire_name, attr_name, intended_value):
    e = etree.parse(file)
    root = e.getroot()
    m = re.match('\{.*\}', root.tag).group(0)
    find_string = ".//" + m + tag + "[@name='" + wire_name + "']"
    node = root.findall(find_string)[0]
    return node.get(attr_name) == intended_value