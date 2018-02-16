def f():
    with open('test', 'w') as f:
        f.write('abc')
    with open('test2', 'w') as f:
        f.write('def')
    with open('test') as f:
        a = f.read()
    with open('test2') as f:
        a += f.read()
    return a


if __name__ == "__main__":
    print(f())  # expected to print abcdef
