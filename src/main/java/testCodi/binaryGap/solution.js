// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N) {
    // write your code in JavaScript (Node.js 8.9.4)
    let binary = (N >>> 0).toString(2);
    let maxGap = 0;
    let previousOne = binary.indexOf("1");
    if (-1 == previousOne) {
        return maxGap;
    }
    binary = binary.substring(previousOne + 1);
    while (binary.length > 0) {
        let currentOne = binary.indexOf("1");
        if (-1 != currentOne) {
            if (maxGap < currentOne) {
                maxGap = currentOne;
            }
            binary = binary.substring(currentOne + 1);
        } else {
            break;
        }
    }
    return maxGap;
}