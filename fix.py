
# Definition of common errors patterns

patterns = {
    r"extraneous input '.0' expecting": {
        "regex_solution": r"\.0",
        "replacement": ""  # Delete '.0'
    },
    # Add more patterns
}

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

def fix_errors(detected_errors):
    for error in detected_errors:
        print(f"Error detected in file {error['full_path']}: {error['message']}")

# Test

syntactic_analysis_report_file = "syntactic_analysis_report.txt"
detected_errors = detect_errors_in_syntactic_analysis_report_file(syntactic_analysis_report_file)
fix_errors(detected_errors)

