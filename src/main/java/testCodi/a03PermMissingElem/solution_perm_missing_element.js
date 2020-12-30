// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution_perm_missing_element(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    if (A.length == 0) {
        return 1;
    }
    A = A.sort();
    if (A[0] != 1) {
        return 1;
    }
    if (A[A.length - 1] != A.length + 1) {
        return A.length + 1;
    }
    for (var index = 1; index <= A.length; index++) {
        if (index < A[index - 1]) {
            return A[index - 1] - 1;
        }
    }
    return 0;
}