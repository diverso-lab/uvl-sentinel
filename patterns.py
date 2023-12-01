patterns = {

    # Delete '.0'
    r"extraneous input '.0' expecting": {
        "regex_solution": r"\.0",
        "replacement": "_0"  
    },

    # Delete '_' before feature names
    r"token recognition error at: '_'": {
        "regex_solution": r"\b_(\w+)",
        "replacement": r"\1"  
    },

    # Delete lines containing only tabs
    r"mismatched input '[\\t]+' expecting": {
        "regex_solution": r"^\t+$\n?",
        "replacement": ""
    },

    # Replace ':' with '_'
    r"token recognition error at: ':'": {
        "regex_solution": r":",
        "replacement": "_"  
    },

    # Replace '/' with '_'
    r"mismatched input '/' expecting": {
        "regex_solution": r"/",
        "replacement": "_" 
    },

    # Replace '-' with '_'
    r"mismatched input '-' expecting": {
        "regex_solution": r"-",
        "replacement": "_" 
    },

    # Replace blank space by underscore in feature names
    r"extraneous input '(\w+)' expecting": {
        "regex_solution": r"(\b\w+\b) (\b\w+\b)",
        "replacement": r"\1_\2"
    },

    # # Delete lines containing only blanks
    r"extraneous input '[ ]+' expecting": {
        "regex_solution": r"^[ ]+$\n?",
        "replacement": ""
    },

    # Add more patterns...
}