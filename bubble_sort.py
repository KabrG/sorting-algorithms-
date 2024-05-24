# Bubble Sort
import random

def bubble_sort(list: list)->None:
    switched = True
        
    while switched:
        switched = False
        
        for i in range(len(list)-1):
           if list[i + 1] < list[i]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                switched = True
    return

def main():
    nums = [random.randint(1, 99) for i in range(10)]
    print(nums)
    bubble_sort(nums)
    print(nums)
                  
if __name__ == "__main__":
    main()

