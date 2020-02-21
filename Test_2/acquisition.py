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
    Tab = []
    Exposure = []
    Brightness = []
    Shutter_speed = []
    ISO = []
    for i in range(1, nb_pic_rasp + 1):
        image_file_rasp = open(str(i) + 'rasp.jpg', 'rb')
        image_file_omx = open(str(i) + 'omx.jpg', 'rb')
        iso_rasp = open(str(i) + 'rasp.jpg', 'rb')
        iso_omx = open(str(i) + 'omx.jpg', 'rb')
        image_rasp = Image(image_file_rasp)
        image_omx = Image(image_file_omx)

        Exposure.append((image_rasp.exposure_time, image_omx.exposure_time))
        Brightness.append((image_rasp.brightness_value, image_omx.brightness_value))
        Shutter_speed.append((image_rasp.shutter_speed_value, image_omx.shutter_speed_value))

        tags = exifread.process_file(iso_rasp)
        s_rasp = tags['EXIF ISOSpeedRatings']
        new_rasp = find_between(repr(s_rasp), '=', ' @')

        tags = exifread.process_file(iso_omx)
        s_omx = tags['EXIF ISOSpeedRatings']
        new_omx = find_between(repr(s_omx), '=', ' @')

        ISO.append((int(new_rasp), int(new_omx)))
    Tab.append(Exposure)
    Tab.append(Brightness)
    Tab.append(Shutter_speed)
    Tab.append(ISO)

    print(' '.rjust(14,'_'), end='')
    for i in range(1, len(ISO) + 1):
        print('| Raspicam, Omxcam ', 'Img' + str(i),' ', end='')
    print('')
    count = 0
    for line in Tab:
        if count == 0:
            print('Exposure'.ljust(13, ' '), end='')
        elif count == 1:
            print('Brightness'.ljust(13,' '), end='')
        elif count == 2:
            print('Shutter_speed'.ljust(13,' '), end='')
        else:
            print('ISO'.ljust(13,' '), end='')
        for element in line:
            print(' |', str(element).rjust(23, ' '), end='')
        print('')
        count += 1

    f = open("file.csv", "w+")
    count = 0
    f.write("Raspicam:")
    for i in range (1, len(Tab[1]) + 1):
        f.write("," + str(i))
    f.write("\n")
    for line in Tab:
        if count == 0:
            f.write("Exposure")
        elif count == 1:
            f.write("Brightness")
        elif count == 2:
            f.write("Shutter_speed")
        else:
            f.write("ISO")
        for element_rasp in line:
            f.write(",%s" % str(element_rasp[0]))
        f.write("\n")
        count += 1
    count = 0
    f.write("\n")
    f.write("Omxcam:")
    for i in range (1, len(Tab[1]) + 1):
        f.write("," + str(i))
    f.write("\n")
    for line in Tab:
        if count == 0:
            f.write("Exposure")
        elif count == 1:
            f.write("Brightness")
        elif count == 2:
            f.write("Shutter_speed")
        else:
            f.write("ISO")
        for element_omx in line:
            f.write(",%s" % str(element_omx[1]))
        f.write("\n")
        count += 1

    f.close()
