require 'rspec'
require 'rspec/autorun'
require_relative('../../../../../src/main/java/testCodi/a03PermMissingElem/solution_perm_missing_element')

RSpec.describe 'perm missing element' do
  describe '#some_method_under_test' do
    subject { perm_missing_element input }

    [
      [[], 1],
      [[2], 1],
      [[1], 2],
      [[1, 2, 3, 4, 5], 6],
      [[2, 3, 4, 5, 6], 1],
      [[2, 3, 1, 5], 4],
      [[1, 2], 3],
      [[3, 1], 2],
      [[3, 2], 1],
      [[2, 3, 4], 1],
      [[4, 2, 3, 5, 1, 6, 8, 9], 7]
    ].each do |input, expected_output|
      it "when the input is #{input}" do
        actual_result = perm_missing_element(input)
        expect(expected_output).to eql perm_missing_element(input)
        # expect(actual_result).to equal(expected_output)
        expect(actual_result).to be == expected_output
      end
    end
  end
end
