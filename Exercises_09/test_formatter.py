# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 16:19:06 2022

@author: Jen
"""

import unittest 
import formatter 

class TestFormatter(unittest.TestCase): 
    
    def test_lower(self): 
        test_text = "JEN BURNS" 
        result = formatter.convert_lower(test_text) 
        self.assertEqual(result, "jen burns") 
        
    def test_upper(self): 
        test_text = "Jen Burns" 
        result = formatter.convert_upper(test_text) 
        self.assertEqual(result, "JeN BURNS") 
        
if __name__ =="__main": unittest.main()