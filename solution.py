def solution(s):
    st1 = ''
    for i in s[::-1]:
        if i.isupper() == True:
            st1 += ' '.join(i) + ' '
        else:
            st1 += i

    return(st1[::-1])


solutions = "breakCamelCase"

print(solution(solutions))