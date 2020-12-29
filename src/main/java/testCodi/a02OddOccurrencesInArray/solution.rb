# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(a)
  # write your code in Ruby 2.2
  a = a.sort
  first_half_sum = 0
  second_half_sum = 0
  index = 0
  while index < a.length
    first_half_sum += a[index]
    if index + 1 < a.length
      second_half_sum += a[index + 1]
    end
    index += 2
  end
  (first_half_sum - second_half_sum).abs()
end
