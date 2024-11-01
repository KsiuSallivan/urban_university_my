for k in range(3,21):
    our_string = ''
    for i in range(1, k):
        for j in range(i+1, k):
            if k % (i+j) == 0:
                our_string += str(i) + str(j)
    print(k, our_string)
