function largestPrimeFactor(number){
let lv = 0;

  while (number % 2 == 0) {
    lv = 2;
    number = Math.floor(number / 2);
  }

  for (let i = 3; i <= Math.sqrt(number); i += 2) {
    while (number % i == 0) {
      lv = i;
      number = Math.floor(number / i);
    }
  }

  if (number > 2) {
    lv = number;
  }

  return lv;
};

console.log(largestPrimeFactor(2))