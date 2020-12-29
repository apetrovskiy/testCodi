require 'param_test'
require 'test/unit'

class MultipleParamsTest < ActiveSupport::TestCase
  param_test "%s includes whitespace is %s", [
    [9, 2], [529, 4], [20, 1], [1041, 5], [15, 0], [32, 0], [1, 0], [5, 1],
    [2_147_483_647, 0], [6, 0], [328, 2], [16, 0], [1024, 0], [11, 1], [19, 2], [42, 1],
    [1162, 3], [51_712, 2], [561_892, 3], [66_561, 9], [6_291_457, 20], [74_901_729, 4],
    [805_306_373, 25], [1_376_796_946, 5], [1_073_741_825, 29], [1_610_612_737, 28]
  ] do |input, expected|
    assert_equal expected, solution_binary_gap(input)
  end
end

# require 'test/unit'
#
# # class SolutionTest < Test::Unit::TestCase
# #     def test_
#
# # require 'rspec'
# # require 'rspec-parameterized'
# require 'rspec/parameterized'
#
# # Nested Array Style
# describe "plus" do
#   where(:input_number, :expected_result) do
#     [
#       [9, 2], [529, 4], [20, 1], [1041, 5], [
#             15, 0], [32, 0], [1, 0], [5, 1],
#         [2147483647, 0], [6, 0], [328, 2], [16, 0], [
#             1024, 0], [11, 1], [19, 2], [42, 1],
#         [1162, 3], [51712, 2], [561892, 3], [
#             66561, 9], [6291457, 20], [74901729, 4],
#         [805306373, 25], [1376796946, 5], [
#             1073741825, 29], [1610612737, 28]
#     ]
#   end
#
#   with_them do
#     it "should do additions" do
#     #   expect(a + b).to eq answer
#       expect(solution input_number).to eq expected_result
#     end
#   end
#
# #   with_them do
# #     # Can browse parameters via `params` method in with_them block
# #     # Can browse all parameters via `all_params` method in with_them block
# #     it "#{params[:a]} + #{params[:b]} == #{params[:answer]}" do
# #       expect(a + b).to eq answer
# #     end
# #   end
# end
