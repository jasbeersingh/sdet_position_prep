# Iterative function to print all distinct subsets of `S`
def findPowerSet(S):
 
    # `N` stores the total number of subsets
    N = int(pow(2, len(S)))
    s = set()
 
    # sort the set
    S.sort()
 
    # generate each subset one by one
    for i in range(N):
        subset = []
        # check every bit of `i`
        for j in range(len(S)):
            # if j'th bit of `i` is set, append `S[j]` to the subset
            if i & (1 << j):
                print(j)
                subset.append(S[j])
            else:
                print(f"else case: {i}, {j}, {1 << j}")
        print("============")
 
        # insert the subset into the set
        s.add(tuple(subset))
 
    # print all subsets present in the set
    print(s)
 
 
if __name__ == '__main__':
 
    # S = [1, 2, 1]
    S = [1,2]
    findPowerSet(S)
