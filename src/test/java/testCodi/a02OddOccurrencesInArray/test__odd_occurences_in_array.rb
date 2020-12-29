# require 'test/unit'

# class SolutionTest < Test::Unit::TestCase
#     def test_

# require 'rspec'
# require 'rspec-parameterized'
require 'rspec-parameterized'

# Nested Array Style
describe 'plus' do
  where(:input_array, :expected_result) do
    [
      [[9, 3, 9, 3, 9, 7, 9], 7],
      [[2, 2, 3, 3, 4], 4],
      [[42], 42]
    ]
  end

  with_them do
    it 'should do additions' do
      #   expect(a + b).to eq answer
      expect(solution(input_array)).to eq expected_result
    end
  end

  #   with_them do
  #     # Can browse parameters via `params` method in with_them block
  #     # Can browse all parameters via `all_params` method in with_them block
  #     it "#{params[:a]} + #{params[:b]} == #{params[:answer]}" do
  #       expect(a + b).to eq answer
  #     end
  #   end
end
