# python3
# Leons Jūlijs Strupītis 13. gr 1k. 221RDB402


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2):
        current = i
        left_child = 2 * current + 1
        right_child = 2 * current + 2
        while left_child < n:
            # Determine the smallest child
            smallest_child = left_child
            if right_child < n and data[right_child] < data[left_child]:
                smallest_child = right_child
            
   
            if data[current] > data[smallest_child]:
                swaps.append((current, smallest_child))
                data[current], data[smallest_child] = data[smallest_child], data[current]
                
               
                current = smallest_child
                left_child = 2 * current + 1
                right_child = 2 * current + 2
            else:
                break
    return swaps

            
def main(): 
    Input = input() 
    if "I" in Input:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n

    if "F" in Input:  
        filepath = "tests/" + input() 
        with open(filepath, 'r') as file:
            n = int(file.readline().strip())
            data = list(map(int, file.readline().strip().split()))
            assert len(data) == n
            
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
        
if __name__ == "__main__":
    main()
