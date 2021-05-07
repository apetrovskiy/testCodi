// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

package testCodi.a01BinaryGap;

@SuppressWarnings("PMD")
class SolutionJ {
    public int solution(int N) {
        // write your code in Java SE 8
        String originalBinary = Integer.toBinaryString(N);
        int maxGap = 0;
        int previousOne = originalBinary.indexOf('1');
        if (-1 == previousOne) {
            return maxGap;
        }
        String binary = originalBinary.substring(previousOne + 1);
        while (binary.length() > 0) {
            int currentOne = binary.indexOf('1');
            if (-1 != currentOne) {
                if (maxGap < currentOne) {
                    maxGap = currentOne;
                }
                binary = binary.substring(currentOne + 1);
                previousOne = currentOne;
            } else {
                break;
            }
        }
        return maxGap;
    }
}
