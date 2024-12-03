calculate_grade <- function(score) {
  if (score >= 90) {
    return("A")
  } else if (score >= 80) {
    return("B")
  } else if (score >= 70) {
    return("C")
  } else {
    return("Fail")
  }
}

# Example usage
score <- as.numeric(readline("Enter the student's score: "))
grade <- calculate_grade(score)
cat("The student's grade is:", grade, "\n")
