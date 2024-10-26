def countPairs(a, b):
    n1 = 0
    n2 = 0
    arrayOfNumbers = []
    a.sort()
    while n1 in range(len(a)):
        while n2 < n1:
            if a[n1] + a[n2] == b:
                arrayOfNumbers.append(f"({a[n1]}, {a[n2]})")
            n2 += 1
        n1 += 1
        n2 = 0
    print(f"Output: {len(set(arrayOfNumbers))}")
    
countPairs([1, 3, 2, 2, 3, 4], 5)
countPairs([1, 1, 1, 1], 2)
countPairs([1, 2, 3, 4, 5], 7)
