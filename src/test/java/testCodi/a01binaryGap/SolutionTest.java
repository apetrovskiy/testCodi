package testCodi.a01BinaryGap;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.params.provider.Arguments.of;

import java.util.stream.Stream;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

public class SolutionTest {
    private SolutionJ cutJava;
    private SolutionKt cutKotlin;

    @BeforeEach
    void setUp() {
        cutJava = new SolutionJ();
        cutKotlin = new SolutionKt();
    }

    @ParameterizedTest
    @MethodSource("getInputData")
    void testBinaryGapJava(int inputNumber, int expectedResult) {
        System.out.println(inputNumber + " " + Integer.toBinaryString(inputNumber) + " " + expectedResult);
        assertEquals(expectedResult, cutJava.solution(inputNumber));
    }

    @ParameterizedTest
    @MethodSource("getInputData")
    void testBinaryGapKotlin(int inputNumber, int expectedResult) {
        System.out.println(inputNumber + " " + Integer.toBinaryString(inputNumber) + " " + expectedResult);
        assertEquals(expectedResult, cutKotlin.solution(inputNumber));
    }

    static Stream<Arguments> getInputData() {
        return Stream.of(of(9, 2), of(529, 4), of(20, 1), of(1041, 5), of(15, 0), of(32, 0), of(1, 0), of(5, 1),
                of(2147483647, 0), of(6, 0), of(328, 2), of(16, 0), of(1024, 0), of(11, 1), of(19, 2), of(42, 1),
                of(1162, 3), of(51712, 2), of(561892, 3), of(66561, 9), of(6291457, 20), of(74901729, 4),
                of(805306373, 25), of(1376796946, 5), of(1073741825, 29), of(1610612737, 28));
    }
}
