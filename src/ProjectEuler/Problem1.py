class Problem1:
    def __init__(self):
        pass

    def Solve(self, input):

        sum = 0

        while input > 0:
            input -= 1
            if input % 3 == 0 or input % 5 == 0:
                sum = sum + input

        return sum
