#!/usr/bin/env python3
"""Hook Z-#1091 voor G5-MEET-E03 (eigen ronde; voorwaardelijk, niet geplaatst). python3 zet.py <basis>"""
import os, sys, runpy
sys.argv = [sys.argv[0], 'G5-MEET-E03', sys.argv[1]]; runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'zet_z1091.py'), run_name='__main__')
