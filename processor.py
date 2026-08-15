from typing import List, Tuple

class Processor:
    def __init__(self, data: List[int]) -> None:
        self.data = data

    def process(self) -> List[int]:
        """
        Process the data by doubling each value.
        
        Returns:
            List[int]: A list of processed integers.
        """
        return [self._double_value(d) for d in self.data]

    def _double_value(self, value: int) -> int:
        """
        Double the given integer value.
        
        Args:
            value (int): The integer to double.
        
        Returns:
            int: The doubled integer value.
        """
        return value * 2

    def get_statistics(self) -> Tuple[int, int]:
        """
        Get the minimum and maximum values from the data.
        
        Returns:
            Tuple[int, int]: Minimum and maximum values.
        """
        return min(self.data), max(self.data) 

