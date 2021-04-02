/*
Given an array of strings, return another array containing all of its longest strings.

Example:
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"]
*/

function allLongestStrings(inputArray) {
    let longestLength = inputArray[0].length;
    
    for (let i = 0; i < inputArray.length; i++) {
        if (inputArray[i].length > longestLength) {
            longestLength = inputArray[i].length;
        }
    }
    
    let result = [];
    
    for (let i = 0; i < inputArray.length; i++) {
        if (inputArray[i].length === longestLength) {
            result.push(inputArray[i]);
        }
    }
    
    return result;
}