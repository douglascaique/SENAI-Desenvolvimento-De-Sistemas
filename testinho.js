// let x = 1
// let a = 3
// let b = 5
// let c = 8
// let d = 7

// let teste1 = !(x>3)&&(x<1)&&!(b>d)
// console.log(teste1)

// let teste2 = !(d<0)&&(c>5)||(x>3)||(c>7)
// console.log(teste2)


// let teste3 = (x>=3)&&!(a<3)&&(a+b==8)
// console.log(teste3)

// let teste4 = !(d>3)||!(b<7)&&!(c>b)
// console.log(teste4)


// let x = 3
// let y = 4
// let z = 5

// if ((x-1) > 2){
//     y++
// } else{
//     y--
// }



// z = x+y
// for (let i = 1; i <= 8; i++) {
//     y = y +1;
    
// }

// z= z+y

// console.log(z)

let n = 4;
let res = 1; // Inicialize com 1 para evitar multiplicação por 0
let cont = 0; // Contador começa em 0
let x = 2;

while (cont < n) { // Executa o loop 'n' vezes
    res = res * x;
    cont++;
}

console.log(res);