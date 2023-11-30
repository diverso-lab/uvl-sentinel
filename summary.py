def count_warnings_and_exceptions(summary_file):
    total_lines = 0
    total_warnings = 0
    total_exceptions = 0

    with open(summary_file, "r") as file:
        for line in file:
            # Ignore header lines
            if "File Name" in line or "Dataset" in line:
                continue

            total_lines += 1

            # Split the line into columns
            parts = line.strip().split(maxsplit=5)  # maxsplit to only split the first few columns
            if len(parts) >= 6:
                warning, exception = parts[3], parts[4]
                if warning == 'True':
                    total_warnings += 1
                if exception == 'True':
                    total_exceptions += 1

    # Avoid division by zero
    if total_lines > 0:
        warning_percentage = (total_warnings / total_lines) * 100
        exception_percentage = (total_exceptions / total_lines) * 100
    else:
        warning_percentage = exception_percentage = 0

    return total_warnings, warning_percentage, total_exceptions, exception_percentage

summary_file = "syntactic_analysis_report.txt" 
warnings, pct_warnings, exceptions, pct_exceptions = count_warnings_and_exceptions(summary_file)

summary_report = f"\nTotal UVL files with warnings: {warnings} ({pct_warnings:.2f}%)\nTotal UVL files with exceptions: {exceptions} ({pct_exceptions:.2f}%)\n"
print(summary_report) 

with open("summary.txt", "a") as summary:
    summary.write(summary_report)

print("Summary generated in 'summary.txt'")