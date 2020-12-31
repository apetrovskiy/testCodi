# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def tape_equilibrium(a)
  # write your code in Ruby 2.2
  sum_left = a[0]
  sum_right = a.inject(0){|sum,x| sum + x } - a[0]
  best_result = (sum_left - sum_right).abs
  (1..(a.length - 2)).each do |index|
    sum_left += a[index]
    sum_right -= a[index]
    current_result = (sum_left - sum_right).abs
    best_result = current_result < best_result ? current_result : best_result
  end
  best_result
end
