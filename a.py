findFirst = lambda list: list[0] if list[0][1] == 0 else findFirst(list[1:])
#findLast = lambda list: list[0] if len(list)==1 else list[1] if list[1][1]>list[0][1] else findLast(list[1:])

findLast= lambda list: list[0] if len(list)==1 else list[0] if list[0][1]>findLast(list[1:])[1] else findLast(list[1:])
