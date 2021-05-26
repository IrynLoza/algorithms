/*
Given an array strings, determine whether it follows the sequence given in the patterns 
array. In other words, there should be no i and j for which strings[i] = strings[j] 
and patterns[i] ≠ patterns[j] or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

Example
For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = true;

For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = false.
*/

function areFollowingPatterns(strings, patterns) {
    for (let i = 0; i < strings.length; i++) {
        if (strings[i] === strings[i+1]) {
            if (patterns[i] === patterns[i+1]) {
                continue;
            } else {
                return false;
            }
        } else {
            if (patterns[i] !== patterns[i+1]) {
                continue;
            } else {
                return false;
            }
        }
    }
    return true;
}

console.log(areFollowingPatterns(["cat", "dog", "dog"], ["a", "b", "b"])) //true
console.log(areFollowingPatterns(["cat", "dog", "doggy"], ["a", "b", "b"])) //false
console.log(areFollowingPatterns(["aaa"], ["aaa"])) //true
console.log(areFollowingPatterns(["aaa", "aaa", "aaa"], ["aaa", "bbb", "aaa"])) //false
console.log(areFollowingPatterns(["re", "jjinh", "rnz", "frok", "frok", "hxytef", "hxytef", 
"frok"], ["kzfzmjwe", "fgbugiomo", "ocuijka", "gafdrts", "gafdrts", "ebdva", "ebdva", "gafdrts"])) //true
