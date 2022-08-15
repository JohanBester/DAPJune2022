// Compound interest
function futureValue(p, r, n, t, i) {
  let amount = 0;
  let principle = p;
  let rate = r;
  let numPerYear = n;
  let years = t;
  let increase = i;
  let rn = rate / numPerYear;

  //first year
  amount = (principle * (1 + rn)) ^ (numPerYear * 1);

  // every following year each year
  for (let repeat = years - 1; repeat > 0; repeat--) {
    principle = amount + increase;
    amount = (principle * (1 + rn)) ^ (n * 1);
  }

  return amount;
}

console.log(futureValue(1000, 0.15, 12, 5, 1000));
