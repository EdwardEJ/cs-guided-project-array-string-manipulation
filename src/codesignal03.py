def validParenthesesSequence(s):
    # left = 0
    # right = len(s) - 1
    # openCount = 0
    # closedCount = 0
    # if len(s) % 2 != 0:
    #     return False
    
    
    # while left < right:
    #     if s[0] == ')' or s[len(s) - 1] == '(':
    #         return False
        
    #     if s[left] == '(':
    #         openCount += 1
    #     if s[left] == ')':
    #         closedCount += 1
    #     if s[right] == ')':
    #         closedCount += 1
    #     if s[right] == '(':
    #         openCount += 1
         
    #     left += 1
    #     right -= 1
        
    # return openCount == closedCount 
        
    stack = []

    
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) > 0:
                # del stack[-1]
                stack.pop()
            else:
                return False
                
    return len(stack) == 0

print(validParenthesesSequence('()()(())'))
print(validParenthesesSequence('()()())'))
print(validParenthesesSequence('())(()'))
print(validParenthesesSequence('(())(())())())(())(('))