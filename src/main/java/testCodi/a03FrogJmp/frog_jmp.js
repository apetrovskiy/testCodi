// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution_frog_jmp(X, Y, D) {
    // write your code in JavaScript (Node.js 8.9.4)
    if (X == Y) {
        return 0;
    }
    let candidate = Math.floor((Y - X) / D);
    if (X + candidate * D >= Y) {
        return candidate;
    } else {
        return candidate + 1;
    }
}

function sum(a, b) {
    return a + b;
}
// module.exports = sum;
// module.exports = solution_frog_jmp;
export { sum, solution_frog_jmp };