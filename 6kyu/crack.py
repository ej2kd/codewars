"""
Crack the PIN
https://www.codewars.com/kata/5efae11e2d12df00331f91a6/train/python
args: string
return: cracked string
"""

import hashlib

def crack(hash):
    result = hashlib.md5(hash).hexdigest()
    return