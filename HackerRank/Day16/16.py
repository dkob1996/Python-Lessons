import math
import os
import random
import re
import sys


try:
    S = input()
    message = int(S)
except Exception as e:
    message = 'Bad String'
finally:
    print(message)