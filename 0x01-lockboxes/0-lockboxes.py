#!/usr/bin/python3

''' python Lockboxes '''

def canUnlockAll(boxes):
    """
    Return True if all boxes can be opened, else return False
    """
    canUnlockAll = False
    keys = {0: True}
    box = len(boxes)
    while(True):
        
        key = len(keys)
        
        for i in range(len(boxes)):
            if boxes[i] and keys.get(i, False):
                for j in boxes[i]:
                    if j < box:
                        keys[j] = True
                    boxes[i] = None
                    
        if not(len(keys) > key):
            break
        
    if key == len(boxes):
        canUnlockAll = True

    return canUnlockAll
