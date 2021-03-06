/*
n children have got m pieces of candy. They want to eat as much candy as 
they can, but each child must eat exactly the same amount of candy as any 
other child. Determine how many pieces of candy will be eaten by all the 
children together. Individual pieces of candy cannot be split.
*/

function candies(m, n) {
    if (m%n === 0) {
        return m/n * n
    } else {
        return Math.floor(m/n) * n
    }
}

console.log(candies(10, 3)) //3
console.log(candies(3, 3)) //3
console.log(candies(10, 7)) //7