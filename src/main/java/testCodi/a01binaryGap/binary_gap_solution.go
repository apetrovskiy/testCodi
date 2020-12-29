package binarygap

// you can also use imports, for example:
// import "fmt"
// import "os"
import "strconv"
import "strings"

// you can write to stdout for debugging purposes, e.g.
// fmt.Println("this is a debug message")

/*func main() {
    inaryGapSolution01(1041)
}*/

// The binary gap solution
func SolutionBinaryGap(N int) int {
    // write your code in Go 1.4
    temp1 := strconv.Itoa(N)
    temp2, _ := strconv.ParseInt(temp1, 10, 64)
    binary := strconv.FormatInt(temp2, 2)

    var maxGap int = 0
    var previousOne = strings.Index(binary, "1")
    if -1 == previousOne {
        return maxGap
    }
    binary = binary[previousOne+1:]
    for len(binary) > 0 {
        var currentOne int = strings.Index(binary, "1")
        if -1 != currentOne {
            if maxGap < currentOne {
                maxGap = currentOne
            }
            binary = binary[currentOne+1:]
        } else {
            break
        }
    }
    return maxGap
}
