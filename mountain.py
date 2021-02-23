#!/usr/bin/env python3

# MIT License
#
# Copyright (c) 2021 Alex M. M.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Creation of a mountain made out of stars
#
# Usage is `python mountain.py <rows>` where `<rows>` is the amount of rows
# to generate. If the argument is not provided, a default of 5 rows is used.

import sys


def generate_line(whitespace_count, star_count):
    whitespace_count = int(whitespace_count)
    if star_count == 0:
        return " " * (whitespace_count * 2)

    result = " " * whitespace_count

    result += "*"
    for _ in range(0, star_count - 1):
        result += " *"

    result += " " * whitespace_count

    return result


def error(*args):
    print("[error]", *args, file=sys.stderr)
    sys.exit(1)


def main(args):
    if len(args) > 1:
        error("Cannot use more than 1 argument")

    amount = 5

    try:
        if len(args) == 1:
            amount = int(args[0])

        if amount == 0:
            error("Cannot create a mountain out of zero rows")
    except ValueError:
        error("Provided argument \"{}\" is not a number".format(args[0]))

    max_chars = amount + (amount - 1)

    for i in range(1, amount + 1):
        print(generate_line(max_chars / 2, i))
        max_chars -= 2


if __name__ == "__main__":
    main(sys.argv[1:])
