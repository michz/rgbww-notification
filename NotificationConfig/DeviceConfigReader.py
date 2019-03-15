import configparser
from .Device import Device
from pathlib import Path

config = configparser.ConfigParser()

def read(path="/etc/rgbww-notification"):
    """
    Reads the configuration files from a given folder
    """

    bulbs = []
    pathlist = Path(path + '/devices').glob('**/*.conf')
    for path in pathlist:
         # because path is object not string
        path_in_str = str(path)
        try:
            device = {}
            config.clear()
            config.read(path_in_str)
            device = Device(
                config['device']['ip'],
                config['device']['name'],
                float(config['device']['factor_r'] or 1.0),
                float(config['device']['factor_g'] or 1.0),
                float(config['device']['factor_b'] or 1.0),
                float(config['device']['factor_ww'] or 1.0),
                float(config['device']['factor_cw'] or 1.0),
            )
            bulbs.append(device)
        except:
            print('Could not parse config file ' + path_in_str)

    return(bulbs)
