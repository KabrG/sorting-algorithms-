import random

def insertion_sort(list: list)->None:
    for i in range(len(list) - 1):
        element = list.pop(i + 1) 
        idx = i + 1
        
        for j in range(i + 1):
            if list[j] > element:
                idx = j
                break

        list.insert(idx, element)
    return

def main():
    nums = [random.randint(1, 99) for i in range(10)]
    print(nums)
    insertion_sort(nums)
    print(nums)

if __name__ == "__main__":
    main()

