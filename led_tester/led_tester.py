# -*- coding: utf-8 -*-

"""Main module."""
import re

class LEDTester:
    
    lights = None
    
    def __init__(self, N):
        self.lights = [[False]*N for _ in range(N)]
        
    def apply(self, led_cmd):
        pass
    def count(self):
        pass