class Problem2:
    def Solve(self, maxFib):
        last = 0
        current = 1
        fibSum = 0

        while last + current < maxFib:
            fib = last + current
            last = current
            current = fib

            if fib % 2 == 0:
                fibSum += fib

        return fibSum
