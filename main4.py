def solution(n: int):
    a,b,c=0,1,0
    for i in range(n):
        c=a+b
        a=b
        b=c
    return b

#Example 1:
print("Example 1:") 
print(solution(n=2))


#Example 2:
print("Example 2:")
print(solution(n=3))
