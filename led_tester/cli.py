# -*- coding: utf-8 -*-

"""Console script for assignment3_led_tester."""
import sys
import click
from utils import *
from led_tester import *
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    
    print("input", input)
    
    N, instructions = parseFile(input)

    ledTester = LEDTester(N)

    for instruction in instructions:
        ledTester.apply(instruction)

    print('#occupied: ', ledTester.count()) 
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
