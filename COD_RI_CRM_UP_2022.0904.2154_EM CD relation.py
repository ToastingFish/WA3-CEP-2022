cdo = float(input('current crit DMG: '))        # the max cd needs to be calcuated (total substat count is the same)
emo = float(input('current EM: '))      # the max em needs to ne calculated (total substat count is the same)
def cd_em_balance():
    print('These are the recommended crit DMG to EM ratios: ')
    cd = 50      # stats crit dmg
    cdin = 1 + cd/100       # crit dmg actual increase
    cdr = 6.6       # crit dmg avg roll: 6.6
    em = 0      # stats EM
    emin = 1 + ((em*2.78)/(1400+em))      # EM actual increase
    emr = 20        # EM avg roll: 20
    dmg = emin * cdin
    #print(emin, cdin, dmg)###
    #EM = 0, what is the max cd that cd is still better
    c = 1
    while (c > 0 and cd <= cdo and em <= emo):
        #print('\n')###
        cdn = cd + cdr      # temporary cd for cal
        #print(cdn)###
        emn = em + emr      # temporary em for cal
        #print(emn)###
        emin = 1 + ((em*2.78)/(1400+em))      # EM actual increase
        #print(emin)###
        cdin = 1 + cd/100       # crit dmg actual increase
        #print(cdin)###
        eminn = 1 + ((emn*2.78)/(1400+emn))      # new EM actual increase
        #print(eminn)###
        cdinn = 1 + cdn/100       # new crit dmg actual increase
        #print(cdinn)###
        if (cdin * eminn > cdinn * emin):
            em += emr
            print('crit DMG: ', round(cd,1),'EM: ', round(em))
            c += 1
        else:
            cd += cdr
            #print(c, cd, em, )###
            c += 1
cd_em_balance()
