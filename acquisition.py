#!/usr/bin/env python3

from exif import Image
import os
import exifread
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring

def find_between(s, first, last ):
    start = s.index( first ) + len( first )
    end = s.index( last, start )
    return s[start:end]

def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

if __name__ == "__main__":
    list_files = os.listdir('.')
    nb_pic_rasp = 0
    nb_pic_omx = 0
    for file in list_files:
        if 'rasp.jpg' in file:
            nb_pic_rasp += 1
        if 'omx.jpg' in file:
            nb_pic_omx += 1
    dico = {}
    dico["Exposure"] = []
    dico["Brightness"] = []
    dico["Shutter_speed"] = []
    dico["ISO"] = []
    for i in range(0, nb_pic_rasp):
        image_file_rasp = open(str(i) + 'rasp.jpg', 'rb')
        image_file_omx = open(str(i) + 'omx.jpg', 'rb')
        iso_rasp = open(str(i) + 'rasp.jpg', 'rb')
        iso_omx = open(str(i) + 'omx.jpg', 'rb')
        image_rasp = Image(image_file_rasp)
        image_omx = Image(image_file_omx)

        dico["Exposure"].append((image_rasp.exposure_time, image_omx.exposure_time))
        dico["Brightness"].append((image_rasp.brightness_value, image_omx.brightness_value))
        dico["Shutter_speed"].append((image_rasp.shutter_speed_value, image_omx.shutter_speed_value))

        tags = exifread.process_file(iso_rasp)
        s_rasp = tags['EXIF ISOSpeedRatings']
        new_rasp = find_between(repr(s_rasp), '=', ' @')

        tags = exifread.process_file(iso_omx)
        s_omx = tags['EXIF ISOSpeedRatings']
        new_omx = find_between(repr(s_omx), '=', ' @')

        dico["ISO"].append((int(new_rasp), int(new_omx)))
    for line in dico:
        print(line, " : ", dico[line])
    #e = dict_to_xml('pableau', dico)
    #print(tostring(e))
    #text_file = open('tableur.xml', 'wb')
    #d = tostring(e)
    #text_file.write(d)
    #text_file.close()
