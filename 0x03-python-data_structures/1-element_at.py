#!/usr/bin/python3

# Fetches an element from a list similar to c.

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return
    return my_list[idx]
