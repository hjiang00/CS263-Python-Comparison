def t():
    c = 1
    for i in range(10):
        c = c * i
        
@profile
def test():
    c = 1
    for i in range(100):
        c = c * c

if __name__ == '__main__':
    test()
