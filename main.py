import argparse
import os
from typing import Literal

def print_file_contents(
    kind: Literal["lines", "bytes"],
    N: int | None,
    filename: str
) -> None:
    if os.path.isfile(filename):
        if kind == 'lines':
            try:
                # Open a file for reading with a specific encoding (e.g., 'utf-8')
                with open(filename, 'r', encoding='utf-8') as f:
                    total_lines = 0
                    for line in f:
                        print(line, end='')
                        total_lines += 1
                        if (
                            isinstance(N, int)
                            and total_lines >= N
                        ):
                            break
            # skip files we don't have permission to read
            except PermissionError as e:
                print(f'Could not open file. Error: "{e}"')
        elif kind == 'bytes':
            try:
                # read file in binary mode
                with open(filename, 'rb') as f:
                    # read the first `N` bytes
                    to_print: bytes = f.read(N)
                    # decode bytes to plain text then print to console
                    to_print_str: str = to_print.decode('utf-8')
                    print(to_print_str, end='')
            # skip files we don't have permission to read
            except PermissionError as e:
                print(f'Could not open file. Error: "{e}"')
        else:
            print(f"{kind} is not a valid read mode!")
    else:
        print(f'"{filename}" is not a valid file!')
    

if __name__ == '__main__':
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Process text file(s).')

    # Add arguments for input file(s)
    parser.add_argument(
        'input_files', 
        nargs='*',  # 0 or more input files
        type=str,
        default=[],
        help='Path to the input file(s). Pass no options with input file to print out the contents of the entire file. Pass no file to read from user input.'
    )

    # Create a mutually exclusive group for -c and -n flags
    group = parser.add_mutually_exclusive_group()

    # Add flags for different options to the mutually exclusive group created above
    group.add_argument('-c', '--bytes', type=int, default=None, help='Print bytes')
    group.add_argument('-n', '--lines', type=int, default=None, help='Print lines')

    # Parse the command-line arguments
    args = parser.parse_args()

    # no params passed, take standard input from user, print it back out
    if (
        args.bytes is None
        and args.lines is None
        and len(args.input_files) == 0
    ):
        for i in range(10):
            print(input())

    # only one input file, no other flags
    elif (
        args.bytes is None
        and args.lines is None
        and len(args.input_files) == 1
    ):
        print_file_contents(
            kind='lines',
            N=None,
            filename=args.input_files[0]
        )

    # only one input file, -n flag for printing lines
    elif (
        args.lines
        and len(args.input_files) == 1
    ):
        print_file_contents(
            kind='lines',
            N=args.lines,
            filename=args.input_files[0]
        )
    
    # only one input file, -c flag for printing bytes
    elif (
        args.bytes
        and len(args.input_files) == 1
    ):
        print_file_contents(
            kind='bytes',
            N=args.bytes,
            filename=args.input_files[0]
        )
    
    # 2 or more input files, no other flags
    elif (
        args.bytes is None
        and args.lines is None
        and len(args.input_files) >= 2
    ):
        for file in args.input_files:
            print(f'==> {file} <==')
            print_file_contents(
                kind='lines',
                N=None,
                filename=file
            )
            print('\n')

    # 2 or more input files, -n flag for printing lines
    elif (
        args.lines
        and len(args.input_files) >= 2
    ):
        for file in args.input_files:
            print(f'==> {file} <==')
            print_file_contents(
                kind='lines',
                N=args.lines,
                filename=file
            )
            print()
    
    # 2 or more input files, -c flag for printing bytes
    elif (
        args.bytes
        and len(args.input_files) >= 2
    ):
        for file in args.input_files:
            print(f'==> {file} <==')
            print_file_contents(
                kind='bytes',
                N=args.bytes,
                filename=file
            )
            print('\n')
    