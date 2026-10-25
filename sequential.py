def sequential_search(array, find_number):
    pos = "Not found"
    for i in range(len(array)):
        if array[i] == find_number:
            pos = i
    return f"{find_number} is Position {pos}"

nilai = [70, 95, 80, 60, 85]
print(sequential_search(nilai, 80))