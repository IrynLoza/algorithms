/*
A little boy is studying arithmetic. He has just learned how to add two 
integers, written one below another, column by column. But he always 
forgets about the important part - carrying.

Given two integers, your task is to find the result which the little boy 
will get.

Note: The boy had learned from this site, so feel free to check it out too 
if you are not familiar with column addition.

Example

For param1 = 456 and param2 = 1734, the output should be
additionWithoutCarrying(param1, param2) = 1180.

   456
  1734
+ ____
  1180
*/

function additionWithoutCarrying(param1, param2) {
    let main;
    let second;
    if (param1 >= param2) {
        main = param1;
        second = param2;
    } else {
        main = param2;
        second = param1;
    };
    
    main = main.toString();
    second = second.toString();
    let index = second.length-1;
    
    let result = '';
    for (let i = main.length-1; i >= 0; i--) {
        if (index >= 0) {
            let num = (+main[i])+(+second[index]);
            let temp = num.toString();
            result = `${temp[temp.length-1]}${result}`;
        } else {
            result = `${main[i]}${result}`;
        }
     
        index--;
    }
    
    return +result;
}

console.log(additionWithoutCarrying(456, 1734)) //1180
console.log(additionWithoutCarrying(9999, 0)) //9999
console.log(additionWithoutCarrying(999, 999)) //888
console.log(additionWithoutCarrying(54321, 56789)) //0

