import os
import sys
import filecmp
from aho_corasick import *
from time import perf_counter

def parse_input_file(input_file_path):
    with open(input_file_path, 'r') as input_file:
        # read the first line containing patterns
        patterns = input_file.readline().strip().split()
        # read the second line containing search strings
        search_string = input_file.readline()
    
    return patterns, search_string

def generate_output_file(output_file_path, patterns, search_str):
    ac = AhoCorasick(patterns)
    results = []

    match = ac.search(search_str)
    for k, v in match.items():
        results.append(f"{k} {' '.join(map(str, v))}")
    
    results.sort()
    with open(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(results))

def run_tests_correctness():
    print("Running correctness test...")
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

def run_tests_time():
    print("Running time test...")
    time_m_dir = 'testfiles/time/time_m'
    time_nz_dir = 'testfiles/time/time_nz'
    automaton_time = {}
    for f in os.listdir(time_m_dir):
        p, s = parse_input_file(os.path.join(time_m_dir, f))
        
        m = int(f.split('.')[0])
        st = perf_counter()
        ac = AhoCorasick(p)
        automaton_time[m] = (perf_counter())-st

    print("\nAUTOMATON TIME:")
    for k, v in automaton_time.items():
        print(k, v)

    search_time = {}
    for f in os.listdir(time_nz_dir):
        p, s = parse_input_file(os.path.join(time_nz_dir, f))
        
        m = int(f.split('.')[0])
        ac = AhoCorasick(p)
        st = perf_counter()
        res = ac.search(s)
        delta_time = (perf_counter())-st

        z = 0
        for v in res.values():
            z+=len(v)
        
        search_time[z] = delta_time

    print("\nSEARCH TIME:")
    for k, v in search_time.items():
        print(k, v)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "t":
            run_tests_time()
        elif arg == "c":
            run_tests_correctness()
        else:
            print("Usage: python your_script.py [t|c]")
    else:
        run_tests_correctness()
        run_tests_time()
