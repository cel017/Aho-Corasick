INPUT_FOLDER = testfile/input
OUTPUT_FOLDER = testfile/output
EXPECTED_FOLDER = testfile/expected

all: clean_output run_tests

clean_output:
	rm -f $(OUTPUT_FOLDER)/*

run_tests:
	python test_ac.py
