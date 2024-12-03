sum_even_numbers <- function(numbers) 
{
  return(sum(numbers[numbers %% 2 == 0]))
}

# Example usage
numbers <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sum_of_evens <- sum_even_numbers(numbers)
cat("The sum of even numbers is:", sum_of_evens, "\n")

