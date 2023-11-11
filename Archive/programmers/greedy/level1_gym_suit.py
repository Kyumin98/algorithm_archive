def solution(n, lost, reserve):
    lost_alter = [x for x in lost if x not in reserve]
    reserve_alter = [x for x in reserve if x not in lost]
    lost = [x for x in lost if x not in reserve]
    
    lost.sort()
    reserve.sort()
    lost_alter.sort()
    for item in lost_alter:
        if item-1 in reserve_alter:
            lost.remove(item)
            reserve_alter.remove(item-1)
        elif item+1 in reserve_alter:
            lost.remove(item)
            reserve_alter.remove(item+1)

    return n - len(lost)
