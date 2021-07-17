/*
A candle factory manufactures two types of candles. A candle is represented 
as either a "///" char sequence (type 1) or an 'O' char (type 2). An empty 
space is represented as a '.' char. Given the description of boxes, how many 
candles of type 1 and type 2 in the boxes?!
Note: A candle of type 1 can be placed vertically or horizontally. A candle of 
type 1 can be broken, in this case, it does not count. A piece of a candle of 
type 1 can be used only once.
*/

function candlesInBox(boxes) {
    console.log(boxes)
}

console.log(candlesInBox([["/O.","..."], 
                        ["/O.","/.."], 
                        ["/..","/O."]])) // [0, 3]
console.log(candlesInBox([["///",".O."], 
                        ["/.O","/..","/..."]])) // [2, 2]  
                        
                        
