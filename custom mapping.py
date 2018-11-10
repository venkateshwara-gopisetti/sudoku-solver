''' '''


arr = [1,2,3,4,3,'_','_',2,2,'_','_',3,4,3,2,1]

arr = ['_',2,3,4,3,'_',1,'_',2,1,'_','_',4,3,2,'_']
#row_no = [x//4 for x in range(len(arr))]
#col_no = [x%4 for x in range(len(arr))]
#block_no = [x+y for x,y in zip([2*(x//2) for x in row_no],[x//2 for x in col_no])]
#
#ord = [(a,x,y,z) for a,x,y,z in zip(arr,row_no,col_no,block_no)]


def block_cont(dr,n):
    return([x[0] for x in dr if x[3]==n])

def col_cont(dr,n):
    return([x[0] for x in dr if x[2]==n])

def row_cont(dr,n):
    return([x[0] for x in dr if x[1]==n])

def calc(x):
    return(4*x[1]+x[2])

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

ord2 = [[arr[x],x//4,x%4,2*(x//4//2)+x%4//2] for x in range(len(arr))]

miss = calc_miss(ord2)

comb = [1,2,3,4]

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
    if list(miss['block'].values()).count(0) == 4:
        return(miss_stack)
    else :
        update(dor,miss)    

