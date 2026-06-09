
DNA=input().strip()
S_LEN=int(input())
counts={}


for i in range (len(DNA) - S_LEN + 1):
    subString = DNA[i:i + S_LEN]
    counts[subString] = counts.get(subString,0) + 1


max_count = max(counts.values())
result = [subString for subString, count in counts.items() if count == max_count]
print(*result)
