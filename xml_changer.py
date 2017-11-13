import xml.etree.ElementTree as etree
import json
from pprint import pprint
import re


def change_element(file, tag, wire_name, attr_name, value, output_file=file):

    etree.register_namespace("", "http://www.ptcusa.com")
    e = etree.parse(file)
    root = e.getroot()
    m = re.match('\{.*\}', root.tag).group(0)
    find_string = ".//" + m + tag + "[@name='" + wire_name + "']"
    node = root.findall(find_string)[0]
    node.set(attr_name, str(value))

    e.write(file, encoding="iso-8859-1", xml_declaration=True)


def verify_change(file, tag, wire_name, attr_name, intended_value):
    e = etree.parse(file)
    root = e.getroot()
    m = re.match('\{.*\}', root.tag).group(0)
    find_string = ".//" + m + tag + "[@name='" + wire_name + "']"
    node = root.findall(find_string)[0]
    return node.get(attr_name) == intended_value

def increment_element(file, tag, wire_name, attr_name, value, output_file=file):
    
    etree.register_namespace("", "http://www.ptcusa.com")
    e = etree.parse(file)
    root = e.getroot()
    m = re.match('\{.*\}', root.tag).group(0)
    find_string = ".//" + m + tag + "[@name='" + wire_name + "']"
    node = root.findall(find_string)[0]
    old_val = node.get(attr_name, default=0)
    node.set(attr_name, str(value + old_val))

    e.write(file, encoding="iso-8859-1", xml_declaration=True)

    return old_val


def verify_increment(file, tag, wire_name, attr_name, intended_value, old_val):
    e = etree.parse(file)
    root = e.getroot()
    m = re.match('\{.*\}', root.tag).group(0)
    find_string = ".//" + m + tag + "[@name='" + wire_name + "']"
    node = root.findall(find_string)[0]
    return node.get(attr_name) == intended_value + old_val
