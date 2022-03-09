def maskify(cc) :
    return '#' * (len(cc) - 4) + cc[-4:]


cc = 'SF$SDfgsd2eA'
r = maskify(cc)
print(r)