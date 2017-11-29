
'''
Universal Character Encoding Detector
Ch15
'''

class UniversalDetector:
    '''
    This handles 5 categories of encoding
    UTF-N
    UTF-16 (Big and Little-Endian)
    UTF-32 (All 4 byte-order variants)

    Escaped encodings
    '''

    '''
    15.3.1
    UTF-n With A BOM#

    If the text starts with a BOM, we can reasonably assume that the text is 
    encoded in UTF-8, UTF-16, or UTF-32. (The BOM will tell us exactly which 
    one; that’s what it’s for.) This is handled inline in UniversalDetector, 
    which returns the result immediately without any further processing. 
    '''