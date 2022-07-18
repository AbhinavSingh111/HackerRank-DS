def removeConsecutiveCharacter(S):
    # approach using stack
    stack=[S[0]]
    for i in range(1,len(S)):
        if stack[-1]==S[i]:
            continue
        else:
            stack.append(S[i])
    
    return "".join(stack)

# another approach

    # a=""
    # for i in range(len(S)-1):
    #     if S[i]!=S[i+1]:
    #         a+=S[i]
    # a+=S[-1]
    # return a
S="aabaa"
print(removeConsecutiveCharacter(S))
