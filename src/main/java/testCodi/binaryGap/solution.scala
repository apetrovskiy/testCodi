package testCodi.binaryGap

import scala.collection.JavaConverters._

// you can write to stdout for debugging purposes, e.g.
// println("this is a debug message")

object Solution {
  def solution(n: Int): Int = {
    // write your code in Scala 2.12
    var binary = Integer.toBinaryString(n)
    var maxGap = 0
    var previousOne = binary.indexOf('1')
    if (-1 == previousOne) {
      return maxGap
    }
    binary = binary.substring(previousOne + 1)
    while (binary.length > 0) {
      var currentOne = binary.indexOf('1')
      if (-1 != currentOne) {
        if (maxGap < currentOne) {
          maxGap = currentOne
        }
        binary = binary.substring(currentOne + 1)
      } else {
        return maxGap
      }
    }
    maxGap
  }
}
