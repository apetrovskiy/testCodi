# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def solution(x, y, d)
  # write your code in Ruby 2.2
  if x == d
    0
  end
  candidate = (y - x).floor / d
  if x + candidate * d >= y
    candidate
  else
    candidate + 1
  end
end
