import os
import re
from patterns import patterns

# Definition of common errors patterns

def detect_errors_in_syntactic_analysis_report_file(syntactic_analysis_report_file):
    errors = []

    with open(syntactic_analysis_report_file, "r") as file:
        next(file)  # Skip headers line
        for line in file:
            parts = line.strip().split(maxsplit=5)
            if len(parts) < 6:
                continue 

            dataset, file_name, full_path, warning, exception, message = parts

            if exception == 'True':
                error_info = {
                    "dataset": dataset,
                    "file_name": file_name,
                    "full_path": full_path,
                    "message": message
                }
                errors.append(error_info)

    return errors

def apply_correction(file_path, error_message):
    # Determine if the error message matches any known patterns
    for pattern, solution in patterns.items():
        if re.search(pattern, error_message):
            with open(file_path, "r") as file:
                content = file.read()

            # Apply correction
            corrected_content = re.sub(solution["regex_solution"], solution["replacement"], content)

            # Prepare the path to the corrected file
            corrected_file_path = file_path.replace("dataset", "corrected_dataset")

            # Create the necessary directories if they do not exist
            os.makedirs(os.path.dirname(corrected_file_path), exist_ok=True)

            # Save the corrected content
            corrected_file_path = file_path.replace("dataset", "corrected_dataset")
            with open(corrected_file_path, "w") as corrected_file:
                corrected_file.write(corrected_content)
            print(f"Corrections applied to {file_path} and saved as {corrected_file_path}")
            return

    print(f"No known pattern found for error in {file_path}: {error_message}")


def fix_errors(detected_errors):
    for error in detected_errors:
        print(f"Error detected in file {error['full_path']}: {error['message']}")
        apply_correction(error['full_path'], error['message'])

# Test

syntactic_analysis_report_file = "syntactic_analysis_report.txt"
detected_errors = detect_errors_in_syntactic_analysis_report_file(syntactic_analysis_report_file)
fix_errors(detected_errors)

