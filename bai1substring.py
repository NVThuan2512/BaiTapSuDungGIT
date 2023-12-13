def lengthOfLongestSubstring(s):
    k = 0
    maxLength = 0
    for i in range(len(s)):
        for j in range(k, i):
            if s[i] == s[j]:
                k = j + 1
                break
        if i - k + 1 > maxLength:
            maxLength = i - k + 1
    return maxLength

n = input("nhap mot chuoi: ")
check = lengthOfLongestSubstring(n)
print(check)