package solution

// you can also use imports, for example:
// import "fmt"
// import "os"
import "sort"

// you can write to stdout for debugging purposes, e.g.
// fmt.Println("this is a debug message")

func Solution(A []int) int {
    // write your code in Go 1.4
    sort.Ints(A)
    var first_half_sum = 0
    var second_half_sum = 0
    for i := 0; i < len(A); i += 2 {
        first_half_sum += A[i]
        if i + 1 < len(A) {
            second_half_sum += A[i + 1]
        }
    }
    var difference = first_half_sum - second_half_sum
    if difference > 0 {
        return difference
    }
    return -difference
}
