/*
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any 
profit, return 0.
*/

function get_max_profit(prices) {
    let profit = 0;
    let buy = prices[0];

    for (let i = 1; i < prices.length; i++) {
       if (buy > prices[i]) {
           buy = prices[i];
       };
       if (profit < prices[i] - buy) {
           profit = prices[i] - buy;
       };

    }
    return profit;
}

console.log(get_max_profit([10, 7, 5, 8, 11, 9])) //6
console.log(get_max_profit([45, 24, 35, 31, 40, 38, 11])) //16
console.log(get_max_profit([7,1,5,3,6,4])) //5
console.log(get_max_profit([7,6,4,3,1])) //0
console.log(get_max_profit([1,2])) //1

