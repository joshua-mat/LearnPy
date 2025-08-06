import numbers

def solution(numbers):
    sol = []
    for i in range(len(numbers)-2):
        if numbers[i] > numbers[i+1] & numbers[i+1] < numbers[i+2]:
           sol.append(1)
        elif numbers[i] < numbers[i+1] & numbers[i+1] > numbers[i+2]:
            sol.append(1)
        else:
            sol.append(0)
    return sol
