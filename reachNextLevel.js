/*
You are playing an RPG game. Currently your experience points (XP) total is 
equal to experience. To reach the next level your XP should be at least at 
threshold. If you kill the monster in front of you, you will gain more 
experience points in the amount of the reward.

Given values experience, threshold and reward, check if you reach the next 
level after killing the monster.
*/

function reachNextLevel(experience, threshold, reward) {
    if (experience+reward >= threshold) {
        return true;
    } else {
        return false;
    }
}

console.log(reachNextLevel(10, 15, 5)) //true
console.log(reachNextLevel(5, 10, 5)) //true
console.log(reachNextLevel(5, 15, 5)) //false