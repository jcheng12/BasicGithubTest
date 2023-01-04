
import sys
sys.path.insert(0, './Dir1')
sys.path.insert(0, './Dir1/Dir1_1')

import os
import test2, test3, test4

print('Test Message (dir: ' + os.getcwd() + ')')
test2.test2_func()
test3.test3_func()
test4.test4_func()