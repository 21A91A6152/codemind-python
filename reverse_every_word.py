def reverse(n):
    return ' '.join(word[::-1] for word in n.split(" "))
n=input()
print(reverse(n))   