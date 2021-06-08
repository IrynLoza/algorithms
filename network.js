/*
input [[5, ON], [7, OFF], [30, ON], [32, OFF], [34, ON]]
output [[5,7], [30,32]]
*/
const ON = 1;
const OFF = 0;
function findOffTimeStamps(arr) {
    let result = [];

    let i = 0;
    while (i < arr.length) {
        let temp = [];
        if (arr[i][1] === ON) {
            if (i < arr.length-1) {
                temp.push(arr[i][0]);
                temp.push(arr[i+1][0]);
                result.push(temp);
                i+= 2;
            }  else {
                break;
            }
        } else {
            i++;
        }
    }
    return result;
}

console.log(findOffTimeStamps([[5, ON], [7, OFF], [30, ON], [32, OFF], [34, ON]])) 
// [[5,7], [30,32]]