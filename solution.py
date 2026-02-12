import pandas as pd
import re

#Regex for strict column name validation (letters and underscores only)
COL_PATTERN = r"[a-zA-Z_]+"

# Pattern to parse the 'role' expression with support for optional whitespace
# Groups: 1: left_column, 2: operator (+, -, *), 3: right_column
ROLE_PATTERN = r"^\s*([a-zA-Z_]+)\s*([\+\-\*])\s*([a-zA-Z_]+)\s*$"

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:

    # Check if the new column name is valid
    if not isinstance(new_column, str) or not re.fullmatch(COL_PATTERN, new_column):
        return pd.DataFrame([])

    # Check if all existing column names in the DataFrame are valid
    for col in df.columns:
        if not re.fullmatch(COL_PATTERN, str(col)):
            return pd.DataFrame([])

    # Try to match the role string; returns a Match object or None
    match = re.fullmatch(ROLE_PATTERN, role)

    if not match:
        return pd.DataFrame([])

    # If match exists, we extract the captured groups
    col_left, operator, col_right = match.groups()

    # Verify if the columns referenced in 'role' are actually present in the DataFrame
    if col_left not in df.columns or col_right not in df.columns:
        return pd.DataFrame([])

    # Create a copy of the original DataFrame to avoid modifying it in place
    result_df = df.copy()


    try:
        if operator == '+':
            result_df[new_column] = df[col_left] + df[col_right]
        elif operator == '-':
            result_df[new_column] = df[col_left] - df[col_right]
        elif operator == '*':
            result_df[new_column] = df[col_left] * df[col_right]

        return result_df
    except Exception:
        # Return an empty DataFrame in case of data type mismatches or other calculation errors
        return pd.DataFrame([])