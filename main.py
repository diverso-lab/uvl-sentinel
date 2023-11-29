import os
import subprocess
from antlr4 import CommonTokenStream, FileStream
from uvl.UVLCustomLexer import UVLCustomLexer
from uvl.UVLPythonParser import UVLPythonParser
from antlr4.error.ErrorListener import ErrorListener

# Custom error listener
class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if "\\t" in msg:
            print(f"Warning in UVL: Line {line}:{column} - {msg}")
            return
        else:
            raise Exception(f"Error in UVL: Line {line}:{column} - {msg}")

# Function to process UVL file
def process_uvl_file(file_path):
    try:
        input_stream = FileStream(file_path)
        lexer = UVLCustomLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(CustomErrorListener())

        stream = CommonTokenStream(lexer)
        parser = UVLPythonParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(CustomErrorListener())

        tree = parser.featureModel()
        print(tree.toStringTree(recog=parser))
        return False, False  # No warning, no exception
    except Exception as e:
        print(f"Exception in file {file_path}: {e}")  # Print the exception information
        if "warning" in str(e).lower():
            return True, False  # Warning
        else:
            return False, True  # Exception

# Main logic
headers = f'{"Dataset":<15} {"File Name":<30} {"Warning":<10} {"Exception":<10}\n'
with open("summary.txt", "w") as summary:
    summary.write(headers)
    for i in range(1, 21):
        dir_path = f"dataset/dataset_{i}"
        if os.path.exists(dir_path):
            for file in os.listdir(dir_path):
                if file.endswith(".uvl"):
                    file_path = os.path.join(dir_path, file)
                    print(f"Processing file: {file_path}")  # Print the file being processed
                    warning, exception = process_uvl_file(file_path)
                    summary.write(f'{f"dataset_{i}":<15} {file:<30} {str(warning):<10} {str(exception):<10}\n')

print("Summary generated in 'summary.txt'")
