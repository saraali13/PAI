calculate_tax <- function(income) 
{
  if (income < 30000) {
    return(0)
  } 
  else if (income <= 70000) 
  {
    return(income * 0.10)
  } 
  else if (income <= 100000) 
  {
    return(income * 0.15)
  } 
  else 
  {
    return(income * 0.20)
  }
}

# Example usage
income <- as.numeric(readline("Enter the annual income: "))
tax <- calculate_tax(income)
cat("The applicable tax is: $", tax, "\n")

