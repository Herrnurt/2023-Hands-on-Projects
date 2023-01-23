#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 23:13:07 2023

@author: boladipo
"""

import string as s 

s = {c for c in s.ascii_lowercase if c in 'aeiou'}
print(s)