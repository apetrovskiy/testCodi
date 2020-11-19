package testCodi.binaryGap;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.params.provider.Arguments.of;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

public class SolutionTest {
    private Solution cut;

    @BeforeEach
    void setUp() {
        cut = new Solution();
    }

    @ParameterizedTest
    @MethodSource("getInputData")
    void test(int inputNumber, int expectedResult) {
        assertEquals(expectedResult, cut.solution(inputNumber));
    }

    static Stream<Arguments> getInputData() {
        return Stream.of(
                of(1041, 5),
                of(15, 0),
                of(32, 0)
        );
    }
}
