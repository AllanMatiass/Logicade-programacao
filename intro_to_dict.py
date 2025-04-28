def printa():
    print('a')

def printb():
    print('b')

def main():

    cmd = {
        'a': printa,
        'b': printb
    }
    inp = input('ASAD')
    if inp not in cmd:
        print('dá nao')
        return
    
    cmd[inp]() 