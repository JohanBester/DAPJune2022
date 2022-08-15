# Compound Interest
# A = P(1 + r/n)^nt
# Where:
#   A is the future value of the investment
#   P is the present value of the investment
#   r is the annual rate of compound interest (as a decimal)
#   n is the number of times the interest is compounded per year
#   t is the length of time, in years, of the investment

def futureValue(p, r, n, t):
    amount = float(0)
    principle = float(p)
    rate = float(r)
    numPerYear = float(n)
    timeYears = t

    rn = float(rate / numPerYear)
    print("rate / numPerYear :", rn)
    nt = float(numPerYear * timeYears)
    print("numPerYear * timeYears", nt)

    amount = principle*(1+rn)**nt

    return amount


print(futureValue(1000.00, 0.15, 2, 5))
