# use the short ones first
# sdl: jobs list


class MinHeap:
    
    def __init__(self):
        self.maxsize = 500
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        
        
    def parent(self, pos):
        return pos//2
    
    def leftChild(self, pos):
        return 2*pos
    
    def rightChild(self, pos):
        return (2*pos) + 1 
    
    def isLeaf(self, pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False
   # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
    
    # Function to heapify the node at pos
    def minHeapify(self, pos):

        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
               self.Heap[pos] > self.Heap[self.rightChild(pos)]):

                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))

                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
                    
    def insert(self, element):
        if self.size >= self.maxsize :
            return
        self.size+= 1
        self.Heap[self.size] = element
        
        current = self.size
        
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

def second_pass(time, jobs, minHeap):
    for i in jobs:
        if i[0] == time:
            minHeap.insert(i)
            
            
            
            
def solution(jobs):
    answer = 0
    minHeap = MinHeap()
    
    
    for i in range(1001):
        second_pass(i, jobs, minHeap)  # i = external clock time 
    
    return answer