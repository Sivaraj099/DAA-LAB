A = [16, 17, 4, 3, 5, 2]
def leader(array):
    leaders = []
    L = len(array)
    for i in range(L):
        leader = array[i]
        is_leader = True
        for j in range(i + 1, L):
            if leader < array[j]:
                is_leader = False
                break
        if is_leader:
            leaders.append(leader)
    return leaders
print(leader(A))
