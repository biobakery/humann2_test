
import os

import cfg

def remove_temp_file(file):
    #if cfg.verbose:
    #    print "\nRemove temp file: " + file
    os.remove(file)

