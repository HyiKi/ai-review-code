import review

PROMPT = """
Below is a snippet of code from a merge request for review. Please evaluate the code based on the following criteria:

Syntax and Style: Check for any syntax errors or deviations from standard coding conventions. Highlight any lines of code that do not adhere to the language's best practices for readability and maintainability.
Performance Optimization: Identify any parts of the code that could be optimized for better performance. Suggest specific changes that could improve efficiency, such as optimizing loops, reducing computational complexity, or minimizing memory usage.
Security Practices: Scan the code for common security vulnerabilities, such as SQL injection, cross-site scripting (XSS), or improper handling of user inputs. Recommend secure coding practices where applicable.
Error Handling: Evaluate the code for proper error handling mechanisms. Point out any potential unhandled exceptions or errors that could disrupt the program's execution flow.
Code Quality: Assess the overall quality of the code. Look for code smells, unnecessary complexity, or redundant code that could be simplified or refactored.
Bug Detection: Analyze the code for potential bugs or logical errors that could lead to incorrect behavior. Explain any identified issues and propose fixes.
I would like you to succinctly summarize the diff within 100 words. If applicable, your summary should include a note about alterations to the signatures of exported functions, global data structures and variables, and any changes that might affect the external interface or behavior of the code.
Ensure your feedback is clear, concise, and actionable, offering specific recommendations for improvement where possible.
By the way, If the code is not too problematic, you only need to answer "LGTM".

Code:
"""

if __name__ == "__main__":
    review.main(PROMPT)
