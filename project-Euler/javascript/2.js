function fiboEvenSum(n) {
    let a = 1;
    let b = 2;
    let sum = b;
    let next = a+b;
    
    while (next <= n){
      if (next % 2 == 0){
        sum += next;
        temp = next;
        next += b;
        b = temp;
      }else{
        temp = next;
        next += b;
        b = temp;
      }
    
    }
      return sum;
    }
console.log(fiboEvenSum(8))