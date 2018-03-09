# -*- coding: utf-8 -*-

"""Main module."""
import re

class LEDTester:
    
    lights = None
    
    def __init__(self, N):
        self.lights = [[False]*N for _ in range(N)]
        
    def apply(self, led_cmd):
        
        on_pat = re.compile(".*(turn on)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        off_pat = re.compile(".*(turn off)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        switch_pat = re.compile(".*(switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        on = on_pat.match(led_cmd)
        off = off_pat.match(led_cmd)
        switch = switch_pat.match(led_cmd)
        
        if on:
            point1_x = on.group(2)
            point1_y = on.group(3)
            point2_x = on.group(4)
            point2_y = on.group(5)
            
        elif off:
            point1_x = off.group(2)
            point1_y = off.group(3)
            point2_x = off.group(4)
            point2_y = off.group(5)
            
        elif switch:
            point1_x = switch.group(2)
            point1_y = switch.group(3)
            point2_x = switch.group(4)
            point2_y = switch.group(5)
    
        
    def count(self):
        pass