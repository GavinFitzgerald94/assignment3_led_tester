#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_tester` package."""

import sys
sys.path.append('.')

import pytest

from click.testing import CliRunner

from led_tester import *
from led_tester import cli
from led_tester import utils


@pytest.fixture

def test_command_line_interface():
    """Test the CLI."""
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N is not None

def test_read_file():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 10
    assert instructions == ['turn on 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'switch 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'turn on 2,2 through 7,7\n']
    
def test_read_file_http():
    ifile = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 1000
    assert instructions[0] == 'turn off 660,55 through 986,197'
    
def test_instructions_parsing_turn_on():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    on_pat = re.compile(".*(turn on)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    on = on_pat.match(instructions[0])
    assert on.group(1) == "turn on"
    assert on.group(2) == "0"
    assert on.group(3) == "0"
    assert on.group(4) == "9"
    assert on.group(5) == "9"