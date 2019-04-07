import read_config

import json
import time
import requests

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps

import toolkit_text
import logging_manager

config = read_config.read_config_general()

LCDWIDTH, LCDHEIGHT = 84, 48


def get_BME280():
    url = 'http://' + config['SETTING']['NODEMCU_IP'] + '/bme280'
    try:
        resp = requests.get(url, timeout=3).text
    except requests.exceptions.Timeout as e:
        return None
    else:
        senorDataDict = json.loads(resp)
        return senorDataDict
    
    


def draw_image(size, data):
    '''Draw image, size = (LCD.LCDWIDTH, LCD.LCDHEIGHT), data '''
    # Load default font. or Alternatively load a TTF font.
    #font = ImageFont.load_default()
    font = ImageFont.truetype('visitor2.ttf', 12)

    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new('1', size)

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
    # Draw a white filled box to clear the image.
    draw.rectangle((0, 0, size), outline=255, fill=255)

    temp_value = data['temperature'] if data else '--'
    humi_value = round(data['humidity'], 2) if data else '--'
    pres_value = round(data['pressure'], 2) if data else '--'

    draw.text((2, 0), "{}".format(time.strftime("%H:%M:%S", time.localtime())), font=font)
    draw.text((2, 10), "Temp: {}'C".format(temp_value), font=font)
    draw.text((2, 20), "Humi: {}%".format(humi_value), font=font)
    draw.text((2, 30), "Pres:{}hPa".format(pres_value), font=font)
    return image


def invert_color(image):
    image = image.convert('L')
    image = ImageOps.invert(image)
    image = image.convert('1')
    return image


if __name__ == '__main__':
    _ = get_BME280()
    print(_)
    image = draw_image((LCDWIDTH, LCDHEIGHT), _)
    image.save('asd.bmp')
