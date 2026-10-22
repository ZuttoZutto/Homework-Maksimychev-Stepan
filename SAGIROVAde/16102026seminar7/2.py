"""Task2. Lists"""
import sys


#lines = sys.stdin.read().splitlines()
lines = "1 2 5 7 8 9", "3 4 8 2 10", "10 3 2 8 5"

french = set(map(int, lines[0].split())) if len(lines) > 0 else set()
swimmers = set(map(int, lines[1].split())) if len(lines) > 1 else set()
pianists = set(map(int, lines[2].split())) if len(lines) > 2 else set()

result = sorted((swimmers & pianists) - french)

print(*result)