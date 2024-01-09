import operator

class PriorityQueue:
    def __init__(self, op=operator.le):
        self.op = op
        self.container = []
        
    def push(self, x):
        """ Push an element into the queue """
        self.container.append(x)
        self.__heapify_up(len(self.container)-1)
    
    def pop(self):
        """ Pop an element """
        if 0 == len(self.container):
            return None
        elif 1 == len(self.container):
            x = self.container.pop()
        else:
            x = self.container[0]
            self.container[0] = self.container.pop()
            self.__heapify_down(0)
        return x
    
    def delete(self, x):
        """ Delete an element. 
        Note the complexity is O(n). 
        """
        idx = self.__find(x)
        if 0 > idx:
            return False
        
        if (len(self.container) - 1) != idx:
            last_x = self.container.pop()
            self.container[idx] = last_x
            parent_idx = self.__parent_idx(idx)
            if 0 <= parent_idx and self.op(self.container[idx], self.container[parent_idx]):
                self.__heapify_up(idx)
            else: 
                self.__heapify_down(idx)
        else:
            self.container.pop()
        
        return True
    
    def __parent_idx(self, idx):
        return (idx - 1) // 2

    def __left_child_idx(self, idx):
        return 2 * idx + 1
    
    def __right_child_idx(self, idx):
        return 2 * idx + 2
    
    def __heapify_up(self, idx):
        child_idx = idx
        parent_idx = self.__parent_idx(child_idx)
        while 0 <= parent_idx and self.op(self.container[child_idx], self.container[parent_idx]):
            self.container[parent_idx], self.container[child_idx] = self.container[child_idx], self.container[parent_idx]
            child_idx = parent_idx
            parent_idx = self.__parent_idx(child_idx)
    
    def __heapify_down(self, idx):
        
        num_items = len(self.container)
        
        while True:
            
            left_idx = self.__left_child_idx(idx)
            right_idx = self.__right_child_idx(idx)
            
            # if no children
            if left_idx >= num_items:
                break
            
            # if two children
            if right_idx < num_items:
                child_idx = left_idx if self.op(self.container[left_idx], self.container[right_idx]) else right_idx
            else:
                child_idx = left_idx
            
            if self.op(self.container[idx], self.container[child_idx]):
                break
                
            # exchange current node with child
            self.container[idx], self.container[child_idx] = self.container[child_idx], self.container[idx]
            idx = child_idx
            
    
    
    def __find(self, x) -> int:
        idx_stack = [0]
        while idx_stack:
            idx = idx_stack.pop()
            val_at_idx = self.container[idx]
            if val_at_idx == x:
                return idx
            elif self.op(val_at_idx, x):
                left_idx = self.__left_child_idx(idx)
                right_idx = self.__right_child_idx(idx)
                if right_idx < len(self.container):
                    idx_stack.append(right_idx)
                    idx_stack.append(left_idx)
                elif left_idx < len(self.container):
                    idx_stack.append(left_idx)
        
        return -1
    
    def __len__(self):
        return len(self.container)