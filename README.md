# Priority of Middle Class 
A priority queue is an array where items are associated with their priorities. Items are withdrawn from a priority queue in order of their priorities starting with the highest priority item first. If the maximum priority item is required, then a heap is constructed such than priority of every node is greater than the priority of its children.

A sample class <em>MinHeap</em> in the starter code shows how to implement the priority queue where items can be extracted starting with the lowest priority. The code uses numpy arrays to ensure efficient implementation.

Your goal is to design and implement a heap datastructure <em>MiddleHeap</em> to model a priority queue where the item with the middle priority is withdrawn first. If there are <em>N</em> items in the heap, then the number of items with the priority smaller than the middle priority is always <em>N//2</em>.

First, describe your idea in this readme file, explain how the withdraw and insert operations work and calculate the complexity of these operations. 

Finally, implement <em>MiddleHeap</em> class, test it and submit in file `middle_heap.py`.

