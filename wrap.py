import textwrap

def wrap1(string, max_width):
    new= textwrap.fill(string,max_width)
    return new

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap1(string, max_width)
    print(result)

