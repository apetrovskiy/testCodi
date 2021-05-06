# you can write to stdout for debugging purposes, e.g.
# puts "this is a debug message"

def perm_missing_element(a)
  # write your code in Ruby 2.2
  1 if a.length.zero?

  a = a.sort
  1 if a[0] != 1

  return a.length + 1 if a[a.length - 1] != a.length + 1

  max_value = a.length + 1
  (1..max_value).each do |index|
    return (a[index - 1] - 1) if index < a[index - 1]
  end
  0
end
