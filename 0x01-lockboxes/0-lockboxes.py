#!/usr/bin/python3
'''A module for working with lockboxes.
'''

def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    
    # Set of boxes that have been unlocked
    seen_boxes = set([0])
    
    # Set of keys we have found but not yet used to unlock boxes
    unseen_boxes = set(boxes[0]).difference(set([0]))
    
    # Process keys until we have no more unused keys
    while unseen_boxes:
        boxIdx = unseen_boxes.pop()
        
        # Ignore invalid box indices
        if boxIdx >= n or boxIdx < 0:
            continue
        
        # If this box has not been unlocked yet
        if boxIdx not in seen_boxes:
            # Add the keys from this box to the set of unused keys
            unseen_boxes.update(boxes[boxIdx])
            
            # Mark this box as unlocked
            seen_boxes.add(boxIdx)
    
    # Check if all boxes have been unlocked
    return len(seen_boxes) == n
