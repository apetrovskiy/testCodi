package a02oddoccurrencesinarray

import "testing"

var testData = []struct {
	in  []int
	out int
}{
	{[] int {9, 3, 9, 3, 9, 7, 9}, 7},
	{[] int {2, 2, 3, 3, 4}, 4},
	{[] int {42}, 42},
}

func TestOddOccurrencesInArray(t *testing.T) {
	for _, td := range testData {
		if td.out != SolutionOddOccurrencesInArray(td.in) {
			t.Errorf("FAIL!")
		}
	}
}
