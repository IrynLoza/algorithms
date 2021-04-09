/*
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
*/

function addBorder(picture) {
    let border = '';
    
    let n = picture[0].length+2;
    while (n > 0) {
        border = `${border}*`
        n--
    }

    for (let i = 0; i < picture.length; i++) {
        picture[i] = `*${picture[i]}*`
    }
    
    picture.push(border)
    picture.unshift(border)
    
    return picture
}

console.log(addBorder(["abc", "ded"])); //["*****","*abc*","*ded*","*****"]