import random


def selection_sort(list: list)->None:
    for i in range(len(list)):
        lowest_num = list[i]
        idx = i

        for j in range(len(list) - i):
            if list[j+i] < lowest_num:
                lowest_num = list[j+i]
                idx = j + i

        temp = list[i]
        list[i] = lowest_num
        list[idx] = temp


def main()->None:
    nums = [random.randint(1, 99) for i in range(10)]
    print(nums)
    selection_sort(nums)
    print(nums)
                  
if __name__ == "__main__":
    main()


