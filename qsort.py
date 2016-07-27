# sample input
input_list=[67,45,42,37,92,83,53,5,9,4,1,11,6,22,25,1,23,99,75,23,2,76,56,26]


def qsort():
    global input_list
    qsort_sub(0, len(input_list)-1)
    print input_list
    
def qsort_sub(l, r):
    global input_list
    sub_len = r-l+1
    init_l = l
    init_r = r
    print "===== SUB ===== size:", sub_len
    p = r
    while (r != l):
        print "l-p-r", l, p, r
        if (p == l):
            # check right side of the pivot
            if (input_list[p] > input_list[r]):
                # swap pivot
                t = input_list[p]
                input_list[p] = input_list[r]
                input_list[r] = t
                p = r
            else:
                r = r - 1
        else:
            # check left side of the pivot
            if (input_list[p] < input_list[l]):
                # swap pivot
                t = input_list[p]
                input_list[p] = input_list[l]
                input_list[l] = t
                p = l
            else:
                l = l + 1
    
    # sort left and right of the pivot
    if (p > init_l+1):
        qsort_sub(init_l, p-1)
    if (p < init_r-1):
        qsort_sub(p+1, init_r)
    
# main
qsort()
