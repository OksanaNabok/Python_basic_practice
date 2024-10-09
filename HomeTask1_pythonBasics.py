import random
import statistics as s

#Create a python script:
#create list of 100 random numbers from 0 to 1000
list_of_randoms=[random.randint(0, 1000) for i in range(100)]

#sort list from min to max (without using sort())
def bubble_sort(arr):
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
print("Unsorted list is:")
print(list_of_randoms)

bubble_sort(list_of_randoms)

print("Sorted list is:")
print(list_of_randoms)

#calculate average for even and odd numbers
list_even=[i for i in list_of_randoms if i%2==0]
list_odd=[i for i in list_of_randoms if i%2!=0]
#using standard aproach
even_avg=float(sum(list_even) / len(list_even))
#using 'staticstics' module
odd_avg=s.mean(list_odd)

#print both average result in console
print(f"Even average: {even_avg:.3f} \nOdd average: {odd_avg:.3f} ")

#Each line of code should be commented with description.