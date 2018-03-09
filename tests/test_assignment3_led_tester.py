#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_tester` package."""

import sys
sys.path.append('.')

import pytest

from click.testing import CliRunner

from led_tester import *
from assignment3_led_tester import cli


@pytest.fixture

def test_command_line_interface():
    """Test the CLI."""
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N is not None