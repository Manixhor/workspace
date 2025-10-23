mdict = {"apple": 3, "banana": 2, "cherry": 1}

sorteditems = dict(sorted(mdict.items(),key=lambda x: x[1]))

print(sorteditems)