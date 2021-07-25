// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    let result = 0;
    A.sort((a, b) => a - b);
    for (let value of A) {
        if (value > 0) {
            if (value > result + 1) {
                return result + 1;
            }
            if (value > result) {
                result = value;
            }
        }
    }
    return result + 1;
}

module.exports = { solution };