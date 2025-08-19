# nums = [1,1,2,2,3]
# multipleNums = []
# freqCount = dict()
# for num in nums:
#     freqCount[num] = freqCount.get(num, 0) + 1
# for (num, freq) in freqCount.items():
#     if freq > 1: multipleNums.append(num)
# print(multipleNums)

#Reverse a String
num = []


def isPalindrome( s: str) -> bool:
    s = ''.join(c.lower() for c in s if c.isalnum())
    l,r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            return False
    l += 1
    r -= 1
    
    return True

print(isPalindrome("Hellolleh"))