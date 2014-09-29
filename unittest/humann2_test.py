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
        help="directory containing HUMAnN2\n[REQUIRED]",
        metavar="<humann2/>",
        required=True)

    return parser.parse_args()


def main():
    # Parse arguments from command line
    args=parse_arguments(sys.argv)

    # Add humann2 and src directory to python path
    sys.path.append(args.humann2)
    sys.path.append(os.path.join(args.humann2,"src"))

    # Update verbosity based on user input
    verbosity_setting=1
    if args.verbose:
        verbosity_setting=2
        cfg.verbose=True

    directory_of_tests=os.path.dirname(os.path.realpath(__file__))
    
    suite = unittest.TestLoader().discover(directory_of_tests,pattern='test_*.py')
    unittest.TextTestRunner(verbosity=verbosity_setting).run(suite)

if __name__ == '__main__':
    main()
