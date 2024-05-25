#using recursion
def twoSumRecursive(self, numbers, target):
    def recursion(l, r):
         if numbers[r] + numbers[l] == target:
              return [l + 1, r + 1]
         if numbers[r] + numbers[l] > target:
              return recursion(l, r - 1)
         return recursion(l + 1, r)

        return recursion(0, len(numbers) - 1)

#using two pointers
def twoSumPtrs(self, numbers, target):
    l, r = 0, len(numbers) - 1

        while(numbers[r] + numbers[l] != target):
            if numbers[r] + numbers[l] > target:
                r -= 1
            else:
                l += 1

        return [l + 1, r + 1]

