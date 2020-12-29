# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution_binary_gap(n)
  # write your code in Ruby 2.2
  binary = n.to_s(2)
  max_gap = 0
  previous_one = binary.index('1')
  return max_gap if previous_one == -1

  binary = binary[previous_one + 1..-1]

  while binary.length.positive?
    current_one = binary.index('1')
    if current_one != nil
      max_gap = current_one if max_gap < current_one
      binary = binary[current_one + 1..-1]
    else
      break
    end
  end
  max_gap
end
