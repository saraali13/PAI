is_leap_year <- function(year) 
{
  if ((year %% 4 == 0 && year %% 100 != 0) || (year %% 400 == 0)) {
    return(TRUE)
  } 
  else 
  {
    return(FALSE)
  }
}

# Example usage
year <- as.numeric(readline("Enter a year: "))
if (is_leap_year(year)) 
{
  cat(year, "is a leap year.\n")
} 
else 
{
  cat(year, "is not a leap year.\n")
}

