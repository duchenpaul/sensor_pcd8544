import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

import image_generate
import read_config

config_file = 'config.ini'


def get_config(config_file):
    config = read_config.read_config_general(
        configFile=config_file)['SPI config']
    for k, v in config.items():
        config[k] = int(v)
    config.pop('BACKLIGHT')
    return config


class PCD8544_Display():
    """Class for PCD8544_Display"""

    def __init__(self, DC, RST, SCLK, DIN, CS):
        self.disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)
        # Initialize library.
        self.disp.begin(contrast=60)
        # Clear display.
        self.disp.clear()

    def display_image(self, image):
        # Display image.
        self.disp.image(image)
        self.disp.display()


if __name__ == '__main__':
    # print(get_config(config_file))
    pass