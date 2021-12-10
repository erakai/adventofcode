class Board:
    def __init__(self, lines):
        self.nums = self.get_numbers(lines)
        self.marknums = []

    def get_numbers(self, lines):
        nums = []
        for line in lines: 
            for num in line.split():
                nums.append(int(num))
        return nums

    def mark_num(self, num):
        self.marknums.append(num) 

    def has_won(self):
        for i in range(5):
            if self.nums[i] in self.marknums and self.nums[i+5] in self.marknums and self.nums[i+10] in self.marknums and self.nums[i+15] in self.marknums and self.nums[i+20] in self.marknums:
                return True
        for i in range(0, 25, 5):
            if self.nums[i] in self.marknums and self.nums[i+1] in self.marknums and self.nums[i+2] in self.marknums and self.nums[i+3] in self.marknums and self.nums[i+4] in self.marknums:
                return True

        return False

    def calc_score(self):
        total = []
        for num in self.nums:
            if num not in self.marknums: total.append(num)
        return sum(total)

lines = []
with open('day4/input.txt') as file:
    lines = file.readlines()

lines = list(filter(lambda val: val != '\n', lines))
boards = []
for i in range(1, len(lines), 5):
    boards.append(Board(lines[i:i+5]))

for called in lines[0].split(","):
    print(len(boards))
    for b in list(boards):
        b.mark_num(int(called))
        if b.has_won():
            print(called + " * " + str(b.calc_score()) + ": " + str(b.calc_score() * int(called)))
            boards.remove(b)