def palindrome_checker(num):
    strnum = str(num)
    n = len(strnum)
    if n < 2:
        return True
    elif strnum[0] == strnum[-1]:
        return palindrome_checker(strnum[1:-1])
    else:
        return False

print(palindrome_checker(12121))
print(palindrome_checker(1231))
print(palindrome_checker(543))
print(palindrome_checker(245))
print(palindrome_checker(202))