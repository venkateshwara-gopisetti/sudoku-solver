''' '''


#arr = [7,2,6,4,9,3,8,1,5,3,1,5,7,2,8,9,4,6,4,8,9,6,5,1,2,3,7,8,5,2,1,4,7,6,9,3,6,7,3,9,
#     8,5,1,2,4,9,4,1,3,6,2,7,5,8,1,9,4,8,3,6,5,7,2,5,6,7,2,1,4,3,8,9,2,3,8,5,7,9,4,6,1]

fg = [7,2,6,4,9,3,8,1,5,3,1,5,7,2,8,9,4,6,4,8,9,6,5,1,2,3,7,8,5,2,1,4,7,6,9,3,6,7,3,9,
     8,5,1,2,4,9,4,1,3,6,2,7,5,8,1,9,4,8,3,6,5,7,2,5,6,7,2,1,4,3,8,9,2,3,8,5,7,9,4,6,1]

rc = int(len(fg)**0.5)
fcr = int(rc**0.5)

arr = ['_' if x%10==0 else fg[x] for x in range(len(fg))]

def block_cont(dr,n):
    return([x[0] for x in dr if x[3]==n])

def col_cont(dr,n):
    return([x[0] for x in dr if x[2]==n])

def row_cont(dr,n):
    return([x[0] for x in dr if x[1]==n])

def calc(x):
    return(rc*x[1]+x[2])

def solve_block(dor,miss):
    aa = [x for x in miss['block'].keys() if miss['block'][x]==1]
    for ii in aa:
        temp = [x[0] for x in dor if x[3] == ii]
        dor[calc([x for x in dor if x[3] == ii and '_' in x][0])][0]=list(set(comb).difference(set(temp)))[0]
    return(dor)
    
def solve_col(dor,miss):
    aa = [x for x in miss['col'].keys() if miss['col'][x]==1]
    for ii in aa:
        temp = [x[0] for x in dor if x[2] == ii]
        dor[calc([x for x in dor if x[2] == ii and '_' in x][0])][0]=list(set(comb).difference(set(temp)))[0]
    return(dor)

def solve_row(dor,miss):
    aa = [x for x in miss['row'].keys() if miss['row'][x]==1]
    for ii in aa:
        temp = [x[0] for x in dor if x[1] == ii]
        dor[calc([x for x in dor if x[1] == ii and '_' in x][0])][0]=list(set(comb).difference(set(temp)))[0]
    return(dor)

def calc_miss(d):
   miss = {}
   miss['block'] = {i:block_cont(d,i).count('_') for i in range(int(len(arr)**0.5))}
   miss['row'] = {i:row_cont(d,i).count('_') for i in range(int(len(arr)**0.5))}
   miss['col'] = {i:col_cont(d,i).count('_') for i in range(int(len(arr)**0.5))}
   return(miss)

ord2 = [[arr[x],x//rc,x%rc,fcr*(x//rc//fcr)+x%rc//fcr] for x in range(len(arr))]

miss = calc_miss(ord2)

comb = [1,2,3,4,5,6,7,8,9]

miss_stack = []
    
def update(dor,miss,i = [0]):
    i[0] += 1
    print(i[0])
    miss_stack.append([[g[0] for g in dor],miss,i[0]])
    dor = solve_block(dor,miss)
    miss_stack.append([[g[0] for g in dor],miss,i[0]])
    miss = calc_miss(dor)
    dor = solve_col(dor,miss)
    miss_stack.append([[g[0] for g in dor],miss,i[0]])
    miss = calc_miss(dor)
    dor = solve_row(dor,miss)
    miss_stack.append([[g[0] for g in dor],miss,i[0]])
    miss = calc_miss(dor)
    if list(miss['block'].values()).count(0) == rc:
        return(miss_stack)
    else :
        update(dor,miss)    

