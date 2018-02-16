def single_read():
    with open('test') as f:
        return f.read()

if __name__ == "__main__":
    single_read()
