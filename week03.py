import array

arr = array.array('f',[11, 9, -77, 8])
for i in range(len(arr)):
    print(f"{arr[i]:3} {id(arr[i])}")
