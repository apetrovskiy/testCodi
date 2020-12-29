package binarygap

import "testing"

var testData = []struct {
    in  int
    out int
}{
    {9, 2}, {529, 4}, {20, 1}, {1041, 5}, {15, 0}, {32, 0}, {1, 0}, {5, 1},
    {2147483647, 0}, {6, 0}, {328, 2}, {16, 0}, {1024, 0}, {11, 1}, {19, 2}, {42, 1},
    {1162, 3}, {51712, 2}, {561892, 3}, {66561, 9}, {6291457, 20}, {74901729, 4},
    {805306373, 25}, {1376796946, 5}, {1073741825, 29}, {1610612737, 28},
}

func TestBinaryGap(t *testing.T) {
    for _, td := range testData {
        if td.out != Solution01(td.in) {
            t.Errorf("FAIL!")
        }
    }
}
