
import math
stack = []

n=0

while n != "QUIT":
    n = input(f"stack is {stack} :\n")
    n=n.split(" ")
    
    command = n[0].upper()
    
    try:
        value = int(n[1])
    except:
        value = None
        
    
    if command == "PUSH" and value != None:
        stack.append(value)
    elif command == "POP" and len(stack) > 0:
        stack.pop()
    elif command =="SWAP" and len(stack) > 1:
        stack[0],stack[1] = stack[1],stack[0]
    elif command == "DUP" and len(stack) > 0:
        stack.append(stack[-1])
    elif command == "+" and len(stack) > 1:
        stack.append(stack[-2]+stack[-1])
        stack.pop(-2)
        stack.pop(-2)
    elif command == "-" and len(stack) > 1:
        stack.append(stack[-2]-stack[-1])
        stack.pop(-2)
        stack.pop(-2)
    elif command == "*" and len(stack) > 1:
        stack.append(stack[-2]*stack[-1])
        stack.pop(-2)
        stack.pop(-2)
    elif command == "/" and len(stack) > 1:
        stack.append(math.floor(stack[-2]/stack[-1]))
        stack.pop(-2)
        stack.pop(-2)

        
        
        
        

    
    
        
    else:
        print("ERROR")
        break
    
    
   
    
    