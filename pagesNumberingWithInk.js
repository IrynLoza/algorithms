/*
You work in a company that prints and publishes books. You are responsible for designing the 
page numbering mechanism in the printer. You know how many digits a printer can print with 
the leftover ink. Now you want to write a function to determine what the last page of the 
book is that you can number given the current page and numberOfDigits left. A page is 
considered numbered if it has the full number printed on it (e.g. if we are working with 
    page 102 but have ink only for two digits then this page will not be considered numbered).

It's guaranteed that you can number the current page, and that you can't number the last one 
in the book.

Example

For current = 1 and numberOfDigits = 5, the output should be
pagesNumberingWithInk(current, numberOfDigits) = 5.
The following numbers will be printed: 1, 2, 3, 4, 5.

For current = 21 and numberOfDigits = 5, the output should be
pagesNumberingWithInk(current, numberOfDigits) = 22.
The following numbers will be printed: 21, 22.
*/

function pagesNumberingWithInk(current, numberOfDigits) {
    let pages = [];
    
    while (numberOfDigits >= 0) {
        let length = current.toString().length;
        if (numberOfDigits - length >= 0) {
            numberOfDigits-= length;
            pages.push(current);
            current++;
        } else {
            break;
        }
    }
    return pages[pages.length-1];
}

console.log(pagesNumberingWithInk(1, 5)) //5
console.log(pagesNumberingWithInk(21, 5)) //22
console.log(pagesNumberingWithInk(8, 4)) //10
console.log(pagesNumberingWithInk(76, 250)) //166
