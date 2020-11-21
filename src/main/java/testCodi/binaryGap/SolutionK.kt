package testCodi.binaryGap

class SolutionK {
    fun solutiion(N: Int): Int {
        var binary = Integer.toBinaryString(N)
        var maxGap: Int = 0
        var previousOne = binary.indexOf('1')
        if (-1 == previousOne){
            return maxGap;
        }
        binary = binary.substring(previousOne + 1)
        while (binary.isNotEmpty()){
            var currentOne: Int = binary.indexOf('1')
            if (-1 == currentOne){
                if (maxGap < currentOne){
                    maxGap = currentOne
                }
                binary = binary.substring(currentOne + 1)
            } else {
                break
            }
        }
        return maxGap
    }
}
