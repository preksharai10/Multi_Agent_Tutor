import re

class CalculatorTool:
    """
    Basic calculator tool to evaluate arithmetic expressions safely.
    Supports +, -, *, / and parentheses.
    """

    @staticmethod
    def evaluate_expression(expr: str) -> str:
        
        if not re.match(r"^[0-9+\-*/().\s]+$", expr):
            return "Invalid characters in expression."

        try:
            
            result = eval(expr, {"__builtins__": None}, {})
            return str(result)
        except Exception:
            return "Error evaluating expression."
