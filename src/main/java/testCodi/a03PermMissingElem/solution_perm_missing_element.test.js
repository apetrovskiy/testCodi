// import solution_perm_missing_element from "./solution_perm_missing_element.js";
const perm_missing_element = require("./solution_perm_missing_element");

test("test02", () => {
    expect(perm_missing_element([2, 3, 1, 5])).toBe(4);
});