
import os

import config

def remove_temp_file(file):
    if config.verbose:
        print "\nRemove temp file: " + file
    os.remove(file)

