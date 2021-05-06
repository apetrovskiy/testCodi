require 'rspec'
require 'rspec/autorun'
require_relative('../../../../../src/main/java/testCodi/a02OddOccurrencesInArray/odd_occurrences_in_array')

RSpec.describe 'odd occurrences in array' do
  describe '#some_method_under_test' do
    subject { odd_occurrences_in_array input }

    [
      [[9, 3, 9, 3, 9, 7, 9], 7],
      [[2, 2, 3, 3, 4], 4],
      [[42], 42]
    ].each do |input, expected_output|
      it "when the input is #{input}" do
        actual_result = odd_occurrences_in_array(input)
        expect(actual_result).to eql expected_output
        expect(actual_result).to equal(expected_output)
        expect(actual_result).to be == expected_output
      end
    end
  end
end
