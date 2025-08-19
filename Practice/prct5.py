def plusOne( digits: list) -> list:
    num = 0
    n = len(digits)
    for i in range(n - 1, -1, -1):
        print("L5",i, digits[i])
        if digits[i] + 1 != 10:
            print(digits[i])
            digits[i] += 1
            print("L9", digits)
            return digits

        digits[i] = 0

        if i == 0:
            print("L15",i)
            return [1] + digits
        print("L17",digits)

print(plusOne([1,9]))