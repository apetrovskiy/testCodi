namespace testCodi.a01BinaryGap
{
    using System;
    // you can also use other imports, for example:
    // using System.Collections.Generic;

    // you can write to stdout for debugging purposes, e.g.
    // Console.WriteLine("this is a debug message");

    public class Solution
    {
        public int solution(int N)
        {
            // write your code in C# 6.0 with .NET 4.5 (Mono)
            string binary = Convert.ToString(N, 2);
            var maxGap = 0;
            var previousOne = binary.IndexOf('1');
            if (-1 == previousOne)
            {
                return maxGap;
            }
            binary = binary.Substring(previousOne + 1);

            while (binary.Length > 0)
            {
                int currentOne = binary.IndexOf('1');
                if (-1 != currentOne)
                {
                    if (maxGap < currentOne)
                    {
                        maxGap = currentOne;
                    }
                    binary = binary.Substring(currentOne + 1);
                    previousOne = currentOne;
                }
                else
                {
                    break;
                }
            }
            return maxGap;
        }
    }

}