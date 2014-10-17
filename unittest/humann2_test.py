#!/usr/bin/env python

"""
HUMAnN2 : HMP Unified Metabolic Analysis Network 2

HUMAnN2 is a pipeline for efficiently and accurately determining
the coverage and abundance of microbial pathways in a community
from metagenomic data. Sequencing a metagenome typically produces millions
of short DNA/RNA reads.

This software is used to test the HUMAnN2 pipeline.

Dependencies: HUMAnN2

To Run: ./humann2_test.py --humann2 <humann2/>
"""

import os
import sys
import argparse
import unittest
import importlib

import cfg
import utils

def parse_arguments (args):
    """
    Parse the arguments from the user
    """
    parser = argparse.ArgumentParser(
        description="HUMAnN2 Unittest: Test cases for HUMAnN2",
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        "-v","--verbose",
        help="additional output is printed\n",
        action="store_true",
        default=False)
    parser.add_argument(
        "--humann2",
        help="directory containing HUMAnN2\n[DEFAULT: $PYTHONPATH]",
        metavar="<humann2/>")

    return parser.parse_args()


def main():
    # Parse arguments from command line
    args=parse_arguments(sys.argv)

    # look for the humann2 executable in the path if not provided
    if not args.humann2:
        humann2_path=utils.return_exe_path("humann2.py")
        if not humann2_path:
            sys.exit("Please provide the path to humann2.py using the option --humann2.")
    else:
        humann2_path=args.humann2

    # Add humann2 and src directory to python path
    sys.path.append(humann2_path)
    sys.path.append(os.path.join(humann2_path,"src"))

    # Update verbosity based on user input
    verbosity_setting=1
    if args.verbose:
        verbosity_setting=2
        cfg.verbose=True

    directory_of_tests=os.path.dirname(os.path.realpath(__file__))
    
    basic_suite = unittest.TestLoader().discover(directory_of_tests,pattern='basic_tests_*.py')
    advanced_suite = unittest.TestLoader().discover(directory_of_tests, pattern='advanced_tests_*.py')
    full_suite = unittest.TestSuite([basic_suite,advanced_suite])
    
    unittest.TextTestRunner(verbosity=verbosity_setting).run(full_suite)

if __name__ == '__main__':
    main()
