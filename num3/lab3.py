def f(x):
    return x**3 + 8

def main():
    result = f(9)
    print("Result:", result)
    if result > 27:
        print("YAY!")
    if result < 27:
        print("NAY!")

if __name__ == "__main__":
    main() 
