import time
import sys

def main():
    print("Hello from Docker!", flush=True)
    print(f"Python version: {sys.version}", flush=True)
    counter = 0
    while True:
        print(f"alive... ({counter})", flush=True)
        counter += 1
        time.sleep(10)

if __name__ == "__main__":
    main()
