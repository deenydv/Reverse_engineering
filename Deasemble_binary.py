import dis

def disassemble_function(func):
    print(dis.dis(func))

def test_function():
    x = 5
    y = 10
    return x + y

disassemble_function(test_function
