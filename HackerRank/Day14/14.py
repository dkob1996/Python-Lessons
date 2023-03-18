class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = None
    def computeDifference(self):
        n = len(self.__elements)
        for i in range(n-1):
            for j in range(i+1, n):
                difference = abs(self.__elements[i]-self.__elements[j])
                if self.maximumDifference is None or self.maximumDifference < difference:
                    self.maximumDifference = difference
	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)