import random 

def bogo_sort(list: list)->None:
    ordered = False

    while not ordered:
        ordered = True
        random.shuffle(list)

        for i in range(len(list) - 1):
            if list[i + 1] < list[i]:
                ordered = False
                break

    return

def main():
    nums = [random.randint(1, 99) for i in range(10)]
    print(nums)
    bogo_sort(nums)
    print(nums)

if __name__ == "__main__":
    main()


