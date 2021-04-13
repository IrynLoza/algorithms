/*
Call two arms equally strong if the heaviest weights they each are able to 
lift are equal.

Call two people equally strong if their strongest arms are equally strong 
(the strongest arm can be both the right and the left), and so are their 
weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two
are equally strong.
*/

function areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) {
    return (Math.max(yourLeft, yourRight) === Math.max(friendsLeft, friendsRight) && Math.min(yourLeft, yourRight) === Math.min(friendsLeft, friendsRight));
}

console.log(areEquallyStrong(10, 15, 15, 10)) //true
console.log(areEquallyStrong(10, 15, 10, 9)) //false
console.log(areEquallyStrong(10, 15, 5, 20)) //false