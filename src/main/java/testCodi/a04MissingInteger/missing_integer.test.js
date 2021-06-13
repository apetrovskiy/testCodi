const { solution } = require('./missing_integer');

describe.each([
    [
        [1, 3, 6, 4, 1, 2], 5
    ],
    [
        [1, 2, 3], 4
    ],
    [
        [-1, -3], 1
    ],
])('solution(%o) should equal %i', (A, expectedResult) => {
    test(`input = ${A}, returns ${expectedResult}`, () => {
        expect(solution(A)).toEqual(expectedResult);
    });
});