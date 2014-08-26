HUMAnN2 Unittests

This folder contains the code and data files used to run unittests on HUMAnN2.

Requirements to run are:
* HUMAnN2: https://bitbucket.org/biobakery/humann2
* Python (>= v2.7)

To run with default settings:
./humann2_test.py --humann2 $HUMAnN2/

$HUMAnN2/ is the directory that contains the HUMAnN2 codebase.

Running with the optional "--verbose" flag will produce output like the following.
The output describes each test which is run along with if it passes.
The total number of tests run will be printed at the end along with the time required
to run the tests. If any tests fail this will be indicated in the output.

test_count_reads (test_utilities.TestHumann2UtilitiesFunctions) ... ok
test_estimate_unaligned_reads (test_utilities.TestHumann2UtilitiesFunctions) ... ok
test_file_exists_readable (test_utilities.TestHumann2UtilitiesFunctions) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.024s

OK

The unittests are written using the simple test discovery framework added in python v2.7. 
To add new unittests to the test suite place them in a new file named 'test_*.py' containing 
a test class and functions as was done in module test_utilities.  
