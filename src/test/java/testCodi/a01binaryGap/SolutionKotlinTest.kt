/*package testCodi.a01BinaryGap

import org.junit.jupiter.api.Test
import org.junit.runner.RunWith
import kotlin.test.assertEquals
import org.junit.runners.Parameterized

@RunWith(value = Parameterized::class)
class SolutionKotlinTest(
    private val inputNumber: Int,
    private val expectedResult: Int
) {
//    @Test
    fun testBinaryGap() {
        val actualResult = SolutionK().solutiion(inputNumber)
        assertEquals(expectedResult, actualResult)
    }

    companion object {
        @JvmStatic
        @Parameterized.Parameters(name = "{index}: input({0})={0}, result={1}")
        fun data(): List<Array<Int>> {
            return arrayListOf(
                arrayOf(9, 2), arrayOf(529, 4), arrayOf(20, 1), arrayOf(1041, 5), arrayOf(15, 0), arrayOf(32, 0), arrayOf(1, 0), arrayOf(5, 1),
                arrayOf(2147483647, 0), arrayOf(6, 0), arrayOf(328, 2), arrayOf(16, 0), arrayOf(1024, 0), arrayOf(11, 1), arrayOf(19, 2), arrayOf(42, 1),
                arrayOf(1162, 3), arrayOf(51712, 2), arrayOf(561892, 3), arrayOf(66561, 9), arrayOf(6291457, 20), arrayOf(74901729, 4),
                arrayOf(805306373, 25), arrayOf(1376796946, 5), arrayOf(1073741825, 29), arrayOf(1610612737, 28)
            ).toList()
        }
    }
}
*/
