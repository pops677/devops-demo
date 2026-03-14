import time
import sys

def main():
    print("Hello from Docker!")
    print(f"Python version: {sys.version}")
    counter = 0
    while True:
        print(f"alive... ({counter})")
        counter += 1
        time.sleep(10)

if __name__ == "__main__":
    main()
