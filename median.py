
def quick_select_multiple(arr, ks):
    
    def quick_select_multiple_core(arr, ks, out, filled):
        """ Find the k-th smallest element """
        
        if 0 == len(arr):
            if not all(filled):
                raise ValueError("The input value of k is out of range.")
            return
        
        # choose the last element as a pivot
        pivot = arr[-1]
        
        # divide the remaining elements into 1) < the pivot, 2) >= to the pivot
        arr_lt = []
        arr_ge = []
        for x in arr[:-1]:
            if x < pivot:
                arr_lt.append(x)
            else:
                arr_ge.append(x)
        
        n_lt = len(arr_lt)
        num_k = len(ks)
        filled_lt = [True] * num_k
        filled_ge = [True] * num_k
        ks_ge = [0] * num_k
        for i in range(num_k):
            if filled[i]:
                continue
            
            if n_lt == ks[i]:
                filled[i] = True
                out[i] = pivot
            elif n_lt < ks[i]:
                filled_ge[i] = False
                ks_ge[i] = ks[i] - n_lt - 1
            else:
                filled_lt[i] = False
        
        quick_select_multiple_core(arr_lt, ks, out, filled_lt)
        quick_select_multiple_core(arr_ge, ks_ge, out, filled_ge)
    
    out = [0] * len(ks)
    filled = [False] * len(ks)
    quick_select_multiple_core(arr, ks, out, filled)
    
    return out

def compute_median(arr):
    n = len(arr)
    if 1 == n % 2:
        kth = quick_select_multiple(arr, [n//2])
        out = kth[0]
    else:
        kth = quick_select_multiple(arr, [n//2 - 1, n//2])
        out = 0.5 * (kth[0] + kth[1])
    
    return out