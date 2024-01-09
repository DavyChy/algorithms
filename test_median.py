import random
import statistics
import math
from median import quick_select_multiple, compute_median
random.seed(0)

def test_quick_select():
    
    # iterate multiple times
    for _ in range(100):
        n = random.randint(1, 1000)
        arr = random.choices(range(n * 10), k=n)
        
        # sort the array to get the ground truth
        arr_sorted = sorted(arr)
        
        # the k-th's
        ks = random.sample(range(n), random.randint(1, max(10, n)))
        
        # call the quick select function
        kths = quick_select_multiple(arr, ks)
        
        # check the output
        for i, k in enumerate(ks):
            assert arr_sorted[k] == kths[i]

def test_median():
    
    # iterate multiple times
    for _ in range(100):
        n = random.randint(1, 1000)
        arr = random.choices(range(n * 10), k=n)
        
        # call the quick select function
        median = compute_median(arr)
        
        # check the output
        assert math.isclose(median, statistics.median(arr))