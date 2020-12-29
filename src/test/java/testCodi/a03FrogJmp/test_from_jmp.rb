require 'rspec'
require 'rspec/autorun'
require_relative('../../../../../src/main/java/testCodi/a03FrogJmp/frog_jmp')

RSpec.describe 'frog jmp' do
  describe '#some_method_under_test' do
    subject { solution_frog_jmp x, y, d }

    [
      [10, 85, 30, 3],
      [10, 234_342_345, 8, 29_292_792],
      [10, 234_342_345, 1, 234_342_335],
      [10, 2_234_342_345, 1, 2_234_342_335],
      [10, 2_234_342_345, 1_000_000_000, 3],
      [100, 100, 2, 0]
    ].each do |x, y, d, expected_output|
      it "when the input is #{x} #{y} #{d}" do
        actual_result = solution_frog_jmp(x, y, d)
        expect(expected_output).to eql solution_frog_jmp(x, y, d)
        # expect(actual_result).to equal(expected_output)
        expect(actual_result).to be == expected_output
      end
    end
  end
end
