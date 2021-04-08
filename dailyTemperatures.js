/*
Given a list of daily temperatures T, return a list such that, for each day in 
the input, tells you how many days you would have to wait until a warmer 
temperature. If there is no future day for which this is possible, put 0 
instead.

Note: The length of temperatures will be in the range [1, 30000]. Each temperature
will be an integer in the range [30, 100].
*/

function dailyTemperature(T) {
    let stack = [];
    
    for (let i = 0; i < T.length; i++) {
        stack.push(0);
        let count = 0;
        for (let y = i; y < T.length; y ++) {
            if (T[y] > T[i]) {
                stack.pop();
                stack.push(count);
                break;
            } else {
                count++;
            }
        }
    }
    
    return stack;
};

console.log(dailyTemperature([73, 74, 75, 71, 69, 72, 76, 73])); 
// [1, 1, 4, 2, 1, 1, 0, 0]