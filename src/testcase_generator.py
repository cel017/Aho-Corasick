from random import choice, randint
from string import ascii_lowercase
from collections import defaultdict
from test_ac import *

def generate_input(max_length, num_patterns, target_size, input_file_path):
    patterns = [''.join(choice(ascii_lowercase) for _ in range(randint(0, max_length))) for _ in range(num_patterns)]
    target = ''.join(choice(ascii_lowercase) for _ in range(target_size))
    
    with open(input_file_path, 'w') as input_file:
        input_file.write(" ".join(patterns) + "\n")
        input_file.write(target + "\n")

    return patterns, target

def naive_search(patterns, search_str):
    result = defaultdict()
    for pattern in patterns:
        i = 0
        while i < len(search_str):
            if search_str[i:i + len(pattern)] == pattern:
                result[pattern].append(i)
                i += 1 
            else:
                i += 1
    return result

def generate_output_file(output_file_path, patterns, search_str):
    match = defaultdict(list)
    search_str = search_str[0]
    for pattern in set(patterns):
        i = 0
        while i < len(search_str):
            if search_str[i:i + len(pattern)] == pattern:
                match[pattern].append(i)
                i += 1 
            else:
                i += 1
            res = ""
    
    results = []
    for k, v in match.items():
        results.append(f"{k} {' '.join(map(str, v))}")
    results.sort()

    with open(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(results))

if __name__ == '__main__':

    ## random gen input/expected here ##
    for i in range(6, 11):
        generate_input(30, 1000, 10000, f'src/testfiles/input/{i}.txt')
        p, s = parse_input_file(f'src/testfiles/input/{i}.txt')
        generate_output_file(f'src/testfiles/expected/{i}.txt', p, s)

