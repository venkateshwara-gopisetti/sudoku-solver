
with open(r"C:\Users\21410\Downloads\sudoku.txt",'r') as f:
    arr = f.read()

def parse_sud(fe):
    return([[int(x) for x in y.split(',')]for y in fe.split(',\n') ])

def unlist_sud(fe):
    return([x for y in fe for x in y])

#arr = [7,2,6,4,9,3,8,1,5,3,1,5,7,2,8,9,4,6,4,8,9,6,5,1,2,3,7,8,5,2,1,4,7,6,9,3,6,7,3,9,
#     8,5,1,2,4,9,4,1,3,6,2,7,5,8,1,9,4,8,3,6,5,7,2,5,6,7,2,1,4,3,8,9,2,3,8,5,7,9,4,6,1]

#fg = ['_','_',6,4,9,3,8,1,5,'_','_',5,7,2,8,9,4,6,4,8,9,6,5,1,2,3,7,8,5,2,1,4,7,6,9,3,6,7,3,9,
#     8,5,1,2,4,9,4,1,3,6,2,7,5,8,1,9,4,8,3,6,5,7,2,5,6,7,2,1,4,3,8,9,2,3,8,5,7,9,4,6,1]

arr = unlist_sud(parse_sud(arr))

rc = int(len(arr)**0.5)
fcr = int(rc**0.5)

def block_cont(dr,n):
    return([x[0] for x in dr if x[3]==n])

def col_cont(dr,n):
    return([x[0] for x in dr if x[2]==n])

def row_cont(dr,n):
    return([x[0] for x in dr if x[1]==n])

def calc(x):
    return(rc*x[1]+x[2])

def min_miss(dor):
    miss = calc_miss(dor)
    return(min([y for x in miss.values() for y in list(x.values())if y >0]))

def solver_one(dor):
    miss = calc_miss(dor)
    aa = [x for x in miss['block'].keys() if miss['block'][x]==1]
    for ii in aa:
        temp = [x[0] for x in dor if x[3] == ii]
        dor[calc([x for x in dor if x[3] == ii and 0 in x][0])][0]=list(set(comb).difference(set(temp)))[0]
    miss = calc_miss(dor)
    aa = [x for x in miss['col'].keys() if miss['col'][x]==1]
    for ii in aa:
        temp = [x[0] for x in dor if x[2] == ii]
        dor[calc([x for x in dor if x[2] == ii and 0 in x][0])][0]=list(set(comb).difference(set(temp)))[0]
    aa = [x for x in miss['row'].keys() if miss['row'][x]==1]
    for ii in aa:
        temp = [x[0] for x in dor if x[1] == ii]
        dor[calc([x for x in dor if x[1] == ii and 0 in x][0])][0]=list(set(comb).difference(set(temp)))[0]
    return(dor)

def find_miss(l):
    return(list(set(comb).difference(set(l))))

def solver_two(dor):
    miss = calc_miss(dor)
    aa = [x for x in miss['row'].keys() if miss['row'][x]>=2]
    bb = [x for x in miss['row'].keys() if miss['col'][x]>=2]
    for a in aa:
        for b in bb:
            if len(list(set(find_miss([x[0] for x in dor if x[1]==a])).intersection(set(find_miss([x[0] for x in dor if x[2]==b])))))==1:
                [x for x in dor if x[1] == a and x[2] == b][0][0] = list(set(find_miss([x[0] for x in dor if x[1]==a])).intersection(set(find_miss([x[0] for x in dor if x[2]==b]))))[0]
    return(dor)
    
    
def calc_miss(d):
   miss = {}
   miss['block'] = {i:block_cont(d,i).count(0) for i in range(int(len(arr)**0.5))}
   miss['row'] = {i:row_cont(d,i).count(0) for i in range(int(len(arr)**0.5))}
   miss['col'] = {i:col_cont(d,i).count(0) for i in range(int(len(arr)**0.5))}
   return(miss)

ord2 = [[arr[x],x//rc,x%rc,fcr*(x//rc//fcr)+x%rc//fcr] for x in range(len(arr))]

miss = calc_miss(ord2)

comb = [1,2,3,4,5,6,7,8,9]

miss_stack = []

def update(dor,miss,i = [0]):
    i[0] += 1
    print(i[0])
    miss_stack.append([[g[0] for g in dor],miss,i[0]])
    if min_miss(dor) == 1:
        dor = solver_one(dor)
    elif min_miss(dor) == 2:
        dor = solver_two(dor)
    miss_stack.append([[g[0] for g in dor],miss,i[0]])
    miss = calc_miss(dor)
    if list(miss['block'].values()).count(0) == rc:
        return(miss_stack)
    else :
        update(dor,miss)