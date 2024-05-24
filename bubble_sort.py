# Bubble Sort


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
    nums = [4, 3, 324, 43, 2, 3]
    print(nums)
    bubble_sort(nums)
    print(nums)
                  
main()

