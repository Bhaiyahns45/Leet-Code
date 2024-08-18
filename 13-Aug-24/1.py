class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        result = ["1"]
        for i in range(2, n + 1):
            if (i % 3) == 0 and (i % 5) == 0:
                result.append("FizzBuzz")
            elif (i % 3) == 0:
                result.append("Fizz")
            elif (i % 5) == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result


def numberOfSteps(self, num: int) -> int:
    steps = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1

    return steps


numberOfSteps(14)
