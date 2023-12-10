INPUT_FOLDER = testfiles/input
OUTPUT_FOLDER = testfiles/output
EXPECTED_FOLDER = testfiles/expected

all: clean correct time

clean:
	rm -f $(OUTPUT_FOLDER)/*

correct:
	python test_ac.py c

time:
	python test_ac.py t