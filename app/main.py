import sys

def highest_count(input: str) -> tuple[str, int]:
    chars = list(input)
    counts = {}
    for char in chars:
        if char not in counts.keys():
            counts[char] = 1
        else:
            counts[char] += 1
    
    return sorted(counts.items(), key = lambda counts: counts[1])[-1]

def main():
    input = sys.argv[1]
    print(highest_count(input))


if __name__ == "__main__":
    main()
