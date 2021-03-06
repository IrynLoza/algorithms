/*
Some people are standing in a row in a park. There are trees between them which 
cannot be moved. Your task is to rearrange the people by their heights in a 
non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
*/

function sortByHeight(a) {
    // let trees = [];
    // let people = [];
    
    // for (let i = 0; i < a.length; i++) {
    //     if (a[i] === -1) {
    //         trees.push(i);
    //     } else {
    //         people.push(a[i]);
    //     }  
    // }
    // console.log(people)
    // people = people.sort();
    
    
    // for (let i = 0; i < people.length; i++) {
    //     people.splice(trees[i], 0, -1);
        
    // }

    // return people
    
    var treePos = [];
    var  heights = [];
    for(var i = 0; i < a.length; i++) {
      if(a[i] === -1) {
          treePos.push(i);
      } else {
          heights.push(a[i]);
      }
    }
    var sortedHeights = heights.sort(function(aa, bb) {
        return aa - bb;
    });
    for(var j = 0; j < a.length; j++) {
      if(treePos.indexOf(j) !== - 1) {
        sortedHeights.splice(j, 0, -1);
      }
    }
    return sortedHeights;
    
}