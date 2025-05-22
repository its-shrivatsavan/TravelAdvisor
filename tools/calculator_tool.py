from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class CalcTools(BaseModel): # Pydantic Model for the tool's input
    operation: str = Field(..., description="The mathematical operation to perform")
    factor: float = Field(..., description="A factor by which to multiply the result of operation")
    
class CalculateTool(BaseTool):
    name: str = "calculate"
    description: str = "Perform mathematical calculations given an operation and a factor"
    def _run(self, operation: str, factor: float) -> str:
        """
        This will perfrom mathematical calculations.
        
        Parameters:
            - operation (str): A string representing a mathematical operation (eg. "10 + 5"),
            - factor (float): A factor by which to multiply the result of the operation.
        
        Returns:
            - A string representation of the calculation result.
        """
        result = eval(operation) * factor
        return f"The result of '{operation}' multiplied by {factor} is {result}"