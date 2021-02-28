import numbers as np

n1 = input()

n2 = int(n1)
if n2 > 0:
    print(n2)
else:
    n1 = list(n1)
    arr = np.array(n1)
    arr1 = []
    for x in arr:
        arr1.append(x)
    n1 = len(arr1)
    index = [n1 - 1]
    index1 = [n1 - 2]

    if arr1[n1 - 1] < arr1[n1 - 2]:
        arr2 = np.delete(arr1, index1)
    else:
        arr2 = np.delete(arr1, index)


    if arr2[1]=='0':
        print(0)
    else:
      for j in arr2:
       print(j, end="")


