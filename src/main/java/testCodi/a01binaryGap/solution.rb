# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution_binary_gap(n)
    # write your code in Ruby 2.2
  binary = n.to_s(2)
  # puts "original: " + n.to_s
  # puts "original binary: " + binary
  max_gap = 0
  previous_one = binary.index('1')
  if -1 == previous_one
    return max_gap
  end
  binary = binary[previous_one + 1..-1]
  # puts "binary: " + binary

  while binary.length > 0
    # puts binary
    current_one = binary.index('1')
    if nil != current_one
      if max_gap < current_one
        max_gap = current_one
      end
      binary = binary[current_one + 1..-1]
      previous_one = current_one
    else
      break
    end
  end
  max_gap
end
