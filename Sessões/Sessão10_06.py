"""
===============================================

            Generator Expression

===============================================
"""
from sys import getsizeof

list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp  = getsizeof({x * 10 for x in range(1000)})
dic_comp  = getsizeof({x: x * 10 for x in range(1000)})
generator = getsizeof(x * 10 for x in range(1000))

print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dicionario Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {generator} bytes')