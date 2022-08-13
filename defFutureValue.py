def futureValue(p, r, n, t, i):
    amount = float(0)
    principle = float(p)
    rate = float(r)
    numPerYear = float(n)
    years = t
    increase = float(i)
    rn = float(rate / numPerYear)

    # first year
    amount = (principle * (1 + rn)) ^ (numPerYear * 1)

    # every following year each year
    for year in (years - 1):
        principle = amount + increase
        amount = (principle * (1 + rn)) ^ (numPerYear * 1)
    return amount


print(futureValue(1000.00, 0.15, 12, 5, 1000.00))
