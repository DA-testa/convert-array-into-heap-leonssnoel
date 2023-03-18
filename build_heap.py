# python3
# Leons Jūlijs Strupītis 13. gr 1k. 221RDB402

def sift_down(data, i, swaps):
    """
    Sift down the element at index i in the given data array 
    so that the subtree rooted at i becomes a heap.
    """
    n = len(data)
    min_index = i
    l = 2 * i + 1  # index of the left child
    if l < n and data[l] < data[min_index]:
        min_index = l
    r = 2 * i + 2  # index of the right child
    if r < n and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        # swap the elements at indices i and min_index
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(data, min_index, swaps)


def build_heap(data):
    """
    Build a binary heap from the given array data in O(n) time.
    """
    swaps = []
    n = len(data)
    .
    for i in range(n // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps


def main():
    text = input()
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))

    
        assert len(data) == n

    
        swaps = build_heap(data)

    
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
     if "F" in text:
        n = int(input())
        data = list(map(int, input().split()))

    
        assert len(data) == n

    
        swaps = build_heap(data)

    
        print(len(swaps))
        for i, j in swaps:
            print(i, j)



if __name__ == "__main__":
    main()
