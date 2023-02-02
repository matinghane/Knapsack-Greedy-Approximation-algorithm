# Knapsack 
# Pi / Wi

m = 26
Wi = [2, 5, 4, 10, 5, 20]
Pi = [7, 10, 12, 30, 8, 48]


def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

def knapsack(m, Wi, Pi):
    n = len(Wi)
    CU = m
    
    # Pi / Wi
    Pi_Wi = []
    for i in range(n):
        Pi_Wi.append( (Pi[i]/Wi[i]) )

    # sort Pi / Wi from highest to lowest
    sorted_Pi_Wi = sorted(Pi_Wi, reverse=True)

    # get primary index of Pi / Wi by sorted list 
    primary_keys = []
    for i in sorted_Pi_Wi:
        indexes = list_duplicates_of(Pi_Wi, i)
        for x in indexes:
            if x not in primary_keys:
                primary_keys.append( x )

    # table headings: i, Pi, Wi, Pi/Wi, Xi, ΣPi.Xi, ΣWi.Xi, CU
    Xi, sum_PiXi, sum_WiXi = 0, 0, 0
    
    rows = []
    for i in primary_keys:
        # if current CU >= Wi --> Xi = 1

        if Wi[i] <= CU:
            Xi = 1
        else:
            rounded = float(CU/Wi[i])
            if rounded > 0:
                Xi = rounded
            else: 
                Xi = 0

        CU = CU - (Wi[i]*Xi)
        sum_PiXi = sum_PiXi + (Pi[i]*Xi)
        sum_WiXi = sum_WiXi + (Wi[i]*Xi)

        rows.append({
            'i': i,
            'Pi': Pi[i],
            'Wi': Wi[i],
            'Pi-Wi': Pi_Wi[i],
            'Xi': Xi,
            'sum_PiXi': sum_PiXi,
            'sum_WiXi': sum_WiXi,
            'CU': CU,
        })

    return rows 


# for i in knapsack(m, Wi, Pi):
#     print( i )


import tabulate
dataset = knapsack(m, Wi, Pi)
header = dataset[0].keys()
rows =  [x.values() for x in dataset]
print(tabulate.tabulate(rows, header))
