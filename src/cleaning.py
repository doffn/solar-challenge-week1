def clean_dataset(df):
    """
    Cleans the input DataFrame by handling missing values,
    correcting data types, and removing invalid entries.

    Parameters:
    -----------
    df : pd.DataFrame
        Raw dataset to clean.

    Returns:
    --------
    pd.DataFrame
        Cleaned dataset ready for analysis.
    """
    # Drop rows with all NaNs
    df = df.dropna(how='all')

    # Convert timestamp to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

    # Remove rows with invalid timestamps
    df = df.dropna(subset=['Timestamp'])

    return df
