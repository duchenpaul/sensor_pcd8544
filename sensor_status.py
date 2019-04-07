import time
import PIL.ImageOps

import image_generate
import show_in_LCD
import read_config

import backlight_ctrl

config_file = 'config.ini'

config = read_config.read_config_general(configFile=config_file)

LCDWIDTH, LCDHEIGHT = int(config['SCREEN']['LCDWIDTH']), int(config['SCREEN']['LCDHEIGHT'])
REFRESH_INTERVAL = int(config['SETTING']['REFRESH_INTERVAL'])

disp = show_in_LCD.PCD8544_Display(**show_in_LCD.get_config(config_file))

backlight_ctrl.backlight_ctrl(50)

while True:
    t1 = time.time()
    image = image_generate.draw_image((LCDWIDTH, LCDHEIGHT), image_generate.get_BME280())
    disp.display_image(image_generate.invert_color(image))
    t2 = time.time()
    # Remove the running time to make sure it takes exactly <<REFRESH_INTERVAL>> sec every time 
    sleeptime = (REFRESH_INTERVAL - (t2 - t1)) if (REFRESH_INTERVAL - (t2 - t1)) > 0 else 0
    time.sleep(sleeptime)