import array

n = int(input())
arr = map(int , input().split())

# to find an second or third max in an array 

third_max = sorted(set(arr))[-3]

print(third_max)

# you can use it like second_max = sorted(set(arr))[-2] to find second max in an array

