def fizzBuzz(n):
    answer = []
    for i in range(1, n + 1):
        if i % 15 == 0:  # divisible by both 3 and 5
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    return answer

# Test the function
print(fizzBuzz(3))
print(fizzBuzz(5))
print(fizzBuzz(15))