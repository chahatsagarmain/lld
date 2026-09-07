
# lets say we are creating multple parsers 
# we have parser for csv , pdf , txt 

# so we identified 3 functions that are common in both , open , parse , close file 

# the thing is open and close file is redudant in all implementations 

# so we can create abstract class for data parser with concrete open and close implementations 
# and csv and pdf would inherit and only implement parse function 

from abc import ABC , abstractmethod

class DataParserTemplate(ABC):
    """
    The Abstract Class defines a template method that contains a skeleton of
    some algorithm, composed of calls to (usually) abstract primitive operations.

    Concrete subclasses should implement these operations, but leave the template
    method itself unmodified.
    """

    def __init__(self , path : str):
        self._path = path

    @abstractmethod
    def parse(self):
        """
        Primitive operation: Subclasses must implement this to provide
        specific parsing logic.
        """
        pass

    def open(self):
        """
        Concrete operation: Open file step shared by all subclasses.
        """
        print(f"concrete implementation of open file: {self._path}")

    def close(self):
        """
        Concrete operation: Close file step shared by all subclasses.
        """
        print(f"concrete implementation of close file: {self._path}")

    def parse_data(self):
        """
        The Template Method defines the skeleton of the algorithm.
        By orchestrating open, parse, and close, it ensures that the file is
        always properly opened and closed, regardless of the parser type.
        """
        self.open()
        self.parse()
        self.close()

class CSVParser(DataParserTemplate):
    """
    CSVParser specializes the template by implementing CSV-specific parsing.
    """

    def parse(self):
        print("csv parsed")

class PDFParser(DataParserTemplate):
    """
    PDFParser specializes the template by implementing PDF-specific parsing.
    """

    def parse(self):
        print("pdf parsed")

if __name__ == "__main__":
    print("--- Running CSV Parser ---")
    csv_parser = CSVParser("document.csv")
    csv_parser.parse_data()

    print("\n--- Running PDF Parser ---")
    pdf_parser = PDFParser("document.pdf")
    pdf_parser.parse_data()