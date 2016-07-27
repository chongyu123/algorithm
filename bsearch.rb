# binary search not using recursion

def binary_search(num, test_array)
  counter = 0
  low = 0
  high = test_array.length

  while (low <= high) do
    i = ((low + high) / 2).floor
    if num == test_array[i]
      return i
      break
    elsif num < test_array[i]
      high = i
    elsif num > test_array[i]
      low = i
    end
    counter += 1

    # value not found
    if (high - low) <= 1
      return nil
    end

  end
end

test_array = [13, 19, 24, 29, 32, 37, 43]
puts binary_search(24, test_array)
# binary_search(11, test array)?