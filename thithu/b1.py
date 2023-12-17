def timSo(n, k):
    multiples = [str(i) for i in range(1, n + 1) if i % k == 0]
    return multiples

def main():
    t = int(input())
    for i in range(1, t + 1):
        n, k = map(int, input().split())
        result = timSo(n, k)
        print(f"Test {i}: {' '.join(result)}")
        if n < 0 or k <= 0:
            print("INVALID")

if __name__ == "__main__":
    main()