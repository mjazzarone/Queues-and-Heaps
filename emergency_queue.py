class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency  



class MinHeap:
    def __init__(self):
        self.data = []  

    def insert(self, patient: Patient) -> None:
        self.data.append(patient)
        self._heapify_up(len(self.data) - 1)

    def remove_min(self) -> Patient:
        if self.is_empty():
            return None
        if len(self.data) == 1:
            return self.data.pop()

        min_patient = self.data[0]
        self.data[0] = self.data.pop()
        self._heapify_down(0)
        return min_patient

    def peek(self) -> Patient:
        if self.is_empty():
            return None
        return self.data[0]

    def print_heap(self) -> None:
        if self.is_empty():
            print("Heap is empty.")
        else:
            for patient in self.data:
                print(f"{patient.name} (urgency={patient.urgency})")

    def is_empty(self) -> bool:
        return len(self.data) == 0
    
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.data[index].urgency < self.data[parent].urgency:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        size = len(self.data)

        if left < size and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left
        if right < size and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        if smallest != index:
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            self._heapify_down(smallest)




def test_insert_and_peek():
    print("Test 1: Insert and Peek")
    heap = MinHeap()
    heap.insert(Patient("Alice", 5))
    heap.insert(Patient("Bob", 2))
    heap.insert(Patient("Charlie", 3))

    top = heap.peek()
    print(f"Expected: Bob | Actual: {top.name} (urgency={top.urgency})")
    print()


def test_remove_min():
    print("Test 2: Remove Min in Order")
    heap = MinHeap()
    heap.insert(Patient("Alice", 5))
    heap.insert(Patient("Bob", 1))
    heap.insert(Patient("Charlie", 4))
    heap.insert(Patient("David", 2))

    while not heap.is_empty():
        patient = heap.remove_min()
        print(f"Removed: {patient.name} (urgency={patient.urgency})")
    print()


def test_peek_empty():
    print("Test 3: Peek Empty Heap")
    heap = MinHeap()
    result = heap.peek()
    print("Expected: None")
    print(f"Actual: {result}")
    print()


def test_remove_from_empty():
    print("Test 4: Remove from Empty Heap")
    heap = MinHeap()
    result = heap.remove_min()
    print("Expected: None")
    print(f"Actual: {result}")
    print()


def test_duplicate_urgencies():
    print("Test 5: Duplicate Urgencies")
    heap = MinHeap()
    heap.insert(Patient("Anna", 3))
    heap.insert(Patient("Ben", 3))
    heap.insert(Patient("Cara", 3))

    print("Removing patients with same urgency:")
    while not heap.is_empty():
        p = heap.remove_min()
        print(f"{p.name} (urgency={p.urgency})")
    print()


def test_single_element():
    print("Test 6: Single Element Heap")
    heap = MinHeap()
    heap.insert(Patient("Solo", 1))
    print("Peek after insert:")
    p = heap.peek()
    print(f"{p.name} (urgency={p.urgency})")
    print("Remove min:")
    p = heap.remove_min()
    print(f"{p.name} (urgency={p.urgency})")
    print("Check if empty:", heap.is_empty())
    print()



test_insert_and_peek()
test_remove_min()
test_peek_empty()
test_remove_from_empty()
test_duplicate_urgencies()
test_single_element()

# Test your MinHeap class here including edge cases
'''
The first reason a tree is the appropriate structure for the doctor structure is mainly down to the fact that trees are good when dealing with a hierarchy.
We are looking to have show what doctors or nurses are subordinates to other doctors as well as add any when needed.
Each doctor can have two subordinates, represented by the left and right nodes, which creates a typical hierarchy that you would find in a real library.
Trees also contain efficient viewing operations through the preorder, inorder, and postorder methods which give us different ways of viewing the tree 
depending on what we need or want to see first, subordinates or doctors. Also, if the structure grows more complex, a tree can scale to itself handle those cases.
As I mentioned before, the traversal methods help to view trees and perform actions on them in different ways based on what you are looking to do. Preorder is great 
when you need to copy a tree or if you are looking to the whole tree structure. Inorder is good for when you are performing any action that requires the natural order 
of the data. Postorder is good for when you want to delete child nodes before the parent nodes or if you need to combine results before using them on the ther current node.
Heaps help to simulate real-time systems because they provide priority-based scheduling. The heap always ensures that the patient with the highest priority is always at the root,
which makes viewing the highest-priority patient easy. The system also rearranges itself whenever a new patient is added based on their urgency number which helps support a situation
where updates constantly happen.
'''