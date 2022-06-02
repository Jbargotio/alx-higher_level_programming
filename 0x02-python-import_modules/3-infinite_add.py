#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    a = 0
    if len(sys.argv) == 1:
        print("0")
    else:
        for b in range(1, len(sys.argv)):
            a += int(sys.argv[b])
        print(f"{a}")
