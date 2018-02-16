def single_write():
    with open('test', 'w') as f:
        f.write('abc')

if __name__ == "__main__":
    single_write()
