def bubble_sort(arr):    #fungsi bernama bubble sort dengan parameter array
    n = len(arr)         #variable yang menghitung panjang array

    for i in range(n):   #perulangan luar untuk variable i yang di mulai dari 0 sampai n-1 atau sebelum n
        for j in range(n - i - 1): #perulangan dalam untuk variable j yang di mulai dari 0 sampai n-i-1 atau sampai sebelum n-1
            if (arr[j] > arr[j + 1]): #jika nilai sebelah kanan lebih besar dari nilai sebelah kiri
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #perintah pertukaran

                
    return arr

studentgrades = [60, 80, 92, 85, 75]
result = bubble_sort(studentgrades)

print("students grade before sorting: ", studentgrades)
print("students grade after sorting: ", result)