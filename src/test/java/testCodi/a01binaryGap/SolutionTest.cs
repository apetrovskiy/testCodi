namespace testCodi.a01BinaryGap
{
    using System;
    using NUnit.Framework;

    public class SolutionTest
    {
        private Solution cut;

        [SetUp]
        public void SetUp()
        {
            cut = new Solution();
        }

        [TestCase(9, 2)]
        [TestCase(529, 4)]
        [TestCase(20, 1)]
        [TestCase(1041, 5)]
        [TestCase(15, 0)]
        [TestCase(32, 0)]
        [TestCase(1, 0)]
        [TestCase(5, 1)]
        [TestCase(2147483647, 0)]
        [TestCase(6, 0)]
        [TestCase(328, 2)]
        [TestCase(16, 0)]
        [TestCase(1024, 0)]
        [TestCase(11, 1)]
        [TestCase(19, 2)]
        [TestCase(42, 1)]
        [TestCase(1162, 3)]
        [TestCase(51712, 2)]
        [TestCase(561892, 3)]
        [TestCase(66561, 9)]
        [TestCase(6291457, 20)]
        [TestCase(74901729, 4)]
        [TestCase(805306373, 25)]
        [TestCase(1376796946, 5)]
        [TestCase(1073741825, 29)]
        [TestCase(1610612737, 28)]
        public void testBinaryGap(int inputNumber, int expectedResult)
        {
            Console.WriteLine(@"{inputNumber} {} {expectedResult}");
            Assert.AreEqual(expectedResult, cut.solution(inputNumber));
        }
    }
}