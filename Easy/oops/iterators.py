nums = [1,4,5,6,67]

it = iter(nums)

print(next(it))  # or print(it.__next())
print(next(it))

for i in it:
    print(i)



# create own iterator to print topten

class Topten:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:    # condition to stop the for loop for topten
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = Topten()
for j in values:
    print(j)