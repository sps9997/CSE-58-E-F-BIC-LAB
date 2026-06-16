k_mers= input()
seq= input()
length= int(input())


s_kmers= len(k_mers)
s_seq= len(seq)

for i in range (s_seq - s_kmers +1):
    flag = 0

    for j in range (s_kmers):
        if (k_mers[j]!= seq[i+j]):
            flag += 1

    if (flag <= length):
        print(i)
