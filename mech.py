# Given lmin,la,lb,lmax --> Returns mechanism type

def mech(ls,l0,l1,l2,l3):
   
   # Define lmin,la,lb,lmax
    lmin = ls[0]
    lmax = ls[3]
    la , lb = ls[1] , ls[2]

    if lmax > lmin + la + lb:
        print('NOT a mechanism')
    if lmax < lmin + la + lb:
        if lmax + lmin > la + lb:
            print('Triple rocker mechanism')
        if lmax + lmin <= la + lb:
            print('Grashof mechanism')
        if lmax + lmin == la + lb:
            print('Change-point/crossover mechanism')
        elif l1 == lmin or l3 == lmin:
            print('Crank-rocker mechanism')
        elif l0 == lmin:
            print('Drag-link mechanism')
        elif l2 == lmin:
            print('Double-rocker mechanism')