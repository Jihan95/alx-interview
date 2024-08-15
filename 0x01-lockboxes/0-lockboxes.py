#!/usr/bin/python3
"""lockboxes game"""


def canUnlockAll(boxes):
    """check if passed boxes could be open"""
    unlocked = [True] + [False] * (len(boxes) - 1)
    stack = [0]
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)
    return all(unlocked)
