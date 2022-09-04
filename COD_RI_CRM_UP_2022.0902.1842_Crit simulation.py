import random
cr = float(input('Enter the crit rate: '))
times = int(input('Enter the number of times you want to simulte: '))     # number of repetition
def cr_sim(cr, times):
    cr_ary = [None] * 1000
    #print(len(cr_ary))###
    cr_num = cr * 10        # number of crit in the whole array
    #print(cr_num)###
    crt = 0     # no. of times it crit
    nct = 0     # no. of times no crit
    for i in range(1000):
        #print(i)###
        if (i <= cr_num):
                cr_ary[i] = 0      # 0 represents crit
                #print('crit', cr_ary[i])###
        else:
            cr_ary[i] = 1      # 1 represents no crit
            #print('no crit', cr_ary[i])###
    for j in range(times):
        check = random.randint(0,999)
        #print(check)###
        if (cr_ary[check] < 1):
            crt += 1
        else:
            nct += 1 
    print('Crit ', crt, ' times, no crit ', nct, ' times. ')

cr_sim(cr, times)
