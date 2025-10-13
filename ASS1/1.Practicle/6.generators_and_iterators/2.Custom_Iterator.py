class ListIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self   # iterator object itself

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration  # stops iteration when done

# Using the custom iterator
numbers = [10, 20, 30, 40, 50]
my_iter = ListIterator(numbers)

for num in my_iter:
    print(num)
