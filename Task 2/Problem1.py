
DNA= input()
Pattern= input()


count= 0
for i in range(len(DNA)-len(Pattern)+1):
    if DNA[i:i +len(Pattern)] == Pattern:
        count+=1
print(count)
