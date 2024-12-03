from collections import deque

def int_check(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

operator_list = ['+', '-', '*', '/', '%', '^', '~']

def tokenize(string: str):
    queue = deque()
    tokens = string.split() #remove whitespace and append tokens 
    for i in tokens: 
       queue.append(i.strip())
    for i in range(len(queue)): #if the value can be converted to an integer, do it
        if int_check(queue[i]) == True:
            queue[i] = float(queue[i])
        else:
            continue
    for i in queue:
        if (type(i) == float) or (i in operator_list):
            continue
        else:
            raise RuntimeError(f'Invalid token: "{i}"')   
    return queue

def no_input():
    raise RuntimeError('No input.')
def not_enough_operands():
    raise RuntimeError('Not enough operands.')
def division_by_zero():
    raise RuntimeError('Division by zero.')
def too_much_input():
    raise RuntimeError('Too much input.')
def too_many_operands():
    raise RuntimeError('Too many operands.')     

def pre_check(queue):
    required_operands = 1
    for i in range(len(queue)):
        if queue[i] in ['+', '-', '*', '/', '%', '^']:
            required_operands += 1
        elif isinstance(queue[i], float):
            required_operands -= 1
        if required_operands == 0 and i != len(queue) - 1:
            too_much_input()
    if required_operands > 0:
        not_enough_operands()
         
# s = tokenize(' - + -2 3 * 8 7  ') # (-2 + 3) - (7*8) = -55
# t = tokenize('10 3 - 17 4 % ~ ^ 1 +')
# prefix(tokenize('+ 1')) #+ ^ - 10 3 ~ % 17 4 1
def prefix(queue):
    int_queue = []
    reversed_queue = list(reversed(queue))
    if len(queue) == 0:
        no_input()
    
    pre_check(queue)

    for i in range(len(reversed_queue)): #gives index, avoids problem of multiple same values
        if isinstance(reversed_queue[i], float): #if queue[i] is a float, append to int_queue
            int_queue.append(reversed_queue[i]) # append the removed number to int_queue
        else: #if the value is an operator instead of a value  
            if reversed_queue[i] != '~': #has different pop number
                if len(int_queue) >= 2:
                    value1 = int_queue.pop()
                    value2 = int_queue.pop()
                    if '+' == reversed_queue[i]:
                        int_queue.append(value1 + value2)
                    elif '-' == reversed_queue[i]:
                        int_queue.append(value1 - value2)
                    elif '*' == reversed_queue[i]:
                        int_queue.append(value1 * value2)
                    elif '^' == reversed_queue[i]:
                        int_queue.append(value1 ** value2)
                    elif '/' == reversed_queue[i]:
                        if value2 == 0:
                            division_by_zero()
                        else:
                            int_queue.append(value1 / value2)
                    else: #if queue[i] is '%'
                        if value2 == 0:
                            division_by_zero()
                        else:
                            int_queue.append(value1 % value2)
                else:
                    not_enough_operands()
            else: # if '~' == queue[-i]
                if len(int_queue) >= 1:
                    value = int_queue.pop()
                    int_queue.append(value * (-1))
                else:
                    not_enough_operands()
    if len(int_queue) > 1:
        too_much_input() 
    else:
        return float(int_queue[0])

def postfix(queue):
    int_queue = []
    list_queue = list(queue) #takes normal list, starts looping from top
    if len(queue) == 0:
        no_input()
    else:
        for i in range(len(list_queue)): #gives index, avoids problem of multiple same values
            if isinstance(list_queue[i], float): #if queue[i] is a float, append to int_queue
                int_queue.append(list_queue[i]) # append the removed number to int_queue
            else: #if the value is an operator instead of a value  
                if list_queue[i] != '~': #has different pop number
                    if len(int_queue) >= 2:
                        value1 = int_queue.pop()
                        value2 = int_queue.pop()
                        if '+' == list_queue[i]:
                            int_queue.append(value1 + value2)
                        elif '-' == list_queue[i]:
                            int_queue.append(value2 - value1)
                        elif '*' == list_queue[i]:
                            int_queue.append(value1 * value2)
                        elif '^' == list_queue[i]:
                            int_queue.append(value2 ** value1)
                        elif '/' == list_queue[i]:
                            if value1 == 0:
                                division_by_zero()
                            else:
                                int_queue.append(value2 / value1)
                        else: #if queue[i] is '%'
                            if value1 == 0:
                                division_by_zero()
                            else:
                                int_queue.append(value2 % value1)
                    else:
                        not_enough_operands()
                else: # if '~' == queue[-i]
                    if len(int_queue) >= 1:
                        value = int_queue.pop()
                        int_queue.append(value * (-1))
                    else:
                        not_enough_operands()
        if len(int_queue) > 1:
            too_many_operands()
        else:
            return float(int_queue[0])

