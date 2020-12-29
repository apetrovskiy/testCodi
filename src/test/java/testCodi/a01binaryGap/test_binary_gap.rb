require 'test/unit'
require 'rspec'
require 'rspec/autorun'
require_relative('../../../../../src/main/java/testCodi/a01binaryGap/solution')

RSpec.describe 1 do
  it 'test' do
    expect(solution_binary_gap(9)).to be == 2
  end
end

RSpec.describe 'binary gap' do
  describe '#some_method_under_test' do
    subject { solution_binary_gap input }

    [
      [9, 2], [529, 4], [20, 1], [1041, 5], [15, 0], [32, 0], [1, 0], [5, 1],
      [2_147_483_647, 0], [6, 0], [328, 2], [16, 0], [1024, 0], [11, 1], [19, 2], [42, 1],
      [1162, 3], [51_712, 2], [561_892, 3], [66_561, 9], [6_291_457, 20], [74_901_729, 4],
      [805_306_373, 25], [1_376_796_946, 5], [1_073_741_825, 29], [1_610_612_737, 28]
    ].each do |input, expected_output|
      it "when the input is #{input}" do
        # let(:input_value) { input }
        actual_result = solution_binary_gap(input)
        expect(expected_output).to eql solution_binary_gap(input)
        expect(actual_result).to equal(expected_output)
        expect(actual_result).to be == expected_output
      end
    end
  end
end
