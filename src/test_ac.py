import os
import filecmp
from aho_corasick import *

def parse_input_file(input_file_path):
    with open(input_file_path, 'r') as input_file:
        # read the first line containing patterns
        patterns = input_file.readline().strip().split()
        # read the second line containing search strings
        search_strings = input_file.readline().strip().split()
    
    return patterns, search_strings

def generate_output_file(output_file_path, patterns, search_str):
    ac = AhoCorasick(patterns)
    search_str = search_str[0]
    results = []

    match = ac.search(search_str)
    for k, v in match.items():
        results.append(f"{k} {' '.join(map(str, v))}")
    
    results.sort()
    with open(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(results))

def run_tests():
    inp_dir = 'testfiles/input'
    out_dir = 'testfiles/output'
    exp_dir = 'testfiles/expected'
    for f in os.listdir(inp_dir):
        p, s = parse_input_file(os.path.join(inp_dir, f))
        generate_output_file(os.path.join(out_dir, f), p, s)

        eq = filecmp.cmp(os.path.join(out_dir, f), os.path.join(exp_dir, f))
        if eq:
            print(f"Test case passed: {f}")
        else:
            print(f"Test case failed: {f}")

if __name__ == "__main__":
    run_tests()