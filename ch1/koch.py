from turtle import*

def X(n):
    if n>0: L("Y",n)
def Y(n):
    if n>0: L("F+F−F−F+F",n)

def L(s, n):
    for c in s:
        if c =='-': lt(90)
        elif c =='+': rt(90)
        elif c =='X': X(n-1)
        elif c =='Y': Y(n-1)
        elif c == 'F': fd(12)

if __name__ == '__main__':
    X(100)
    mainloop()
