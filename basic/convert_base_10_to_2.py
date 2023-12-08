
def convert_base_10_to_2(num:int)->str:
    stack = []
    data = num
    while data > 0:
        stack.append(data%2)
        data = data //2
        
    result = ''
    while len(stack) > 0:
        result += str(stack.pop())

    return result
    # return f'{num:b}'
    # return f'{num:b}'

def convert_base_10_to_2_str(num:int)->str:
    data = num
    result = ''
    while data > 0:
        result = str(data%2) + result
        data = data //2
        
    return result
 

if __name__ == '__main__':
    num = int(input('Enter base 10 number: '))
    print(num, ' -> ', convert_base_10_to_2(num))
    print(num, ' -> ', convert_base_10_to_2_str(num))