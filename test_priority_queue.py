from priority_queue import PriorityQueue
import random
import operator
random.seed(0)

def test_integer_sort():
    
    for i in range(100):
        arr = random.choices(range(100), k=50)
        
        descending = random.choice([True, False])
        
        # Sort the array as the ground truth for comparison
        arr_sorted = sorted(arr, reverse=not descending)
        
        # Sort with a priority queue
        pq = PriorityQueue(op=operator.gt if descending else operator.lt)
        for x in arr:
            pq.push(x)
        
        # check the output
        while pq:
            x = pq.pop()
            x_gt = arr_sorted.pop()
            assert x == x_gt

def test_string_sort():
    charactors = "abcedfghijklmnopqrstuvwxyz 0123456789!@#$%^&*()`~[];',./{}:<>?\|\""
    
    for i in range(100):
        arr = ["".join(random.choices(charactors, k=random.randint(1, 33))) for j in range(100)]
        
        descending = random.choice([True, False])
        
        # ground truth in reverse order
        arr_sorted = sorted(arr, reverse=not descending)
        
        # Sort with a priority queue
        pq = PriorityQueue(op=operator.gt if descending else operator.lt)
        for x in arr:
            pq.push(x)
        
        # check the output
        while pq:
            x = pq.pop()
            x_gt = arr_sorted.pop()
            assert x == x_gt

def test_pop_empty():
    pq = PriorityQueue()
    assert pq.pop() is None
    
    for i in range(10):
        pq.push(i)
        
    for i in range(10):
        pq.pop()
    
    assert pq.pop() is None
        
def test_delete():
    for i in range(100):
        arr = list(range(100))
        random.shuffle(arr)
        
        pq = PriorityQueue()
        for x in arr:
            pq.push(x)
        
        # items to be deleted
        to_be_deleted = arr[-20:]
        # remaining items
        arr = arr[:-20]
        
        for x in to_be_deleted:
            # successful deletion returns True
            assert pq.delete(x)
            # Return false if delete the same element
            assert not pq.delete(x)
        
        arr_sorted = sorted(arr, reverse=True)
        while pq:
            x = pq.pop()
            x_gt = arr_sorted.pop()
            assert x == x_gt
        
        assert pq.pop() is None