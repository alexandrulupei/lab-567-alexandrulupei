from Domain.vanzarecarte import getTipreducere, creeazaVanzare, getId, getTitlu, getGen, getPret


def discount(lista):
    '''
    Determina reducearea pretului unei vanzari
    :param tipdiscount:
    :param lista:
    :return:
    '''
    listanoua = []
    for vanzare in lista:
        if "silver" in getTipreducere(vanzare):
            vanzarenoua = creeazaVanzare(
                getId(vanzare),
                getTitlu(vanzare),
                getGen(vanzare),
                getPret(vanzare) - (getPret(vanzare) * 0.05),
                getTipreducere(vanzare)
            )
            listanoua.append(vanzarenoua)
        elif "gold" in getTipreducere(vanzare):
            vanzarenoua = creeazaVanzare(
                getId(vanzare),
                getTitlu(vanzare),
                getGen(vanzare),
                getPret(vanzare) - (getPret(vanzare) * 0.1),
                getTipreducere(vanzare)
            )
            listanoua.append(vanzarenoua)
        else:
            listanoua.append(vanzare)
    return listanoua


def getmodificaredupatitlu(title, gen, lista):
    '''
    gaseste o vanzare dupa titlu si o modifica
    :param gen:
    :param title:
    :param lista:
    :return:
    '''
    listanoua = []
    for vanzare in lista:
        if title in getTitlu(vanzare):
            vanzaremod = creeazaVanzare(
                getId(vanzare),
                getTitlu(vanzare),
                gen,
                getPret(vanzare),
                getTipreducere(vanzare)
            )
            listanoua.append(vanzaremod)
        else:
            listanoua.append(vanzare)
    return listanoua