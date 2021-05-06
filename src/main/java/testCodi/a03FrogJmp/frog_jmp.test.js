// const sum = require("./frog_jmp.js");
// import { sum, solution_frog_jmp } from './frog_jmp.js';
const sum = require("./frog_jmp");
const solution_frog_jmp = require("./frog_jmp");

test("test01", () => {
    expect(solution_frog_jmp(1, 2, 1)).toBe(1);
});

test("adds 1 + 2 to equal 3", () => {
    expect(sum(1, 2)).toBe(3);
});