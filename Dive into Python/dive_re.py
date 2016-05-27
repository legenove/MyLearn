__author__ = 'legenove'
import re

pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IV|IX|V?I{0,3})$'
print re.search(pattern, 'MDLV')
print re.search(pattern, 'MMDCLXVI')
print re.search(pattern, 'I')
print re.search(pattern, 'MMMDCCCLXXXVIII')

