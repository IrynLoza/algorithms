/*
Some phone usage rate may be described as follows:

first minute of a call costs min1 cents,
each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
each minute after 10th costs min11 cents.
You have s cents on your account before the call. What is the duration 
of the longest call (in minutes rounded down to the nearest integer) 
you can have?
*/

function phoneCall(min1, min2_10, min11, s) {
    let minutes = 0;
  
    let rate = min1;
    
    while (s > 0) {
        
        minutes += 1;
        
        if (minutes == 2) {
            rate = min2_10;
        } else if (minutes > 10) {
            rate = min11;
        }
        
        s -= rate
        if (s < 0) {
            minutes -= 1;
        }
        
    }    
    return minutes;
}

console.log(phoneCall(3,1,2,20)) //14
console.log(phoneCall(10,10,10,8)) //0
console.log(phoneCall(2,2,1,24)) //14