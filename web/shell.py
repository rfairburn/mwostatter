#!/usr/bin/env python
'''
Run things from the shell
'''

import os
import readline
from pprint import pprint

from flask import *
from app import *

os.environ['PYTHONINSPECT'] = 'True'
