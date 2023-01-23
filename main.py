
import sys
sys.path.insert(0, './Dir1')
sys.path.insert(0, './Dir1/Dir1_1')

import os
import test2, test3, test4

print('Test Message (dir: ' + os.getcwd() + ')')
test2.test2_func()
test3.test3_func()
test4.test4_func()

print('Test Message: I put this here so I would need to do another commit and push')

print('Test Message: Now this is made in test_branch1 before I do a merge')
print('Test Message: Doing an amend before I merge test_branch1 with main')

print('Test Message: Another update after the pull-request to main')

print('Test Message: Now from GitSampleClone, hoping to push back to a local repo')

# Another Comment
# Another Comment after I deleted a bunch of files for Crontab task
# 1-23-2023 Another comment