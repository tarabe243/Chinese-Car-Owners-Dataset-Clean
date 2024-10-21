# Data Cleaning and Processing Script

This Python script is designed for cleaning and processing large CSV datasets. It performs various data cleaning operations, validation checks, and handles large datasets efficiently through chunking.

## Features

1. **Data Cleaning**
   - Handles missing data
   - Removes duplicate entries
   - Converts data types
   - Handles outliers
   - Standardizes data formats

2. **Data Validation**
   - Validates specific fields (e.g., email addresses) using regex

3. **Chunking**
   - Processes large CSV files in smaller chunks to manage memory efficiently
   - Saves intermediate results for each chunk

4. **Header Replacement**
   - Replaces existing headers with a custom list of headers

5. **Logging**
   - Logs processing steps and important information

## Requirements

- Python 3.x
- pandas
- os
- logging
- re

## Usage

1. Place your input CSV file in the same directory as the script.
2. Update the `input_file` variable with your CSV filename.
3. Run the script:

   ```
   python data_cleaning_processing_script.py
   ```

## Input

- A large CSV file containing the data to be cleaned and processed

## Output

The script generates two types of output files:

1. **Clean Data**: 
   - Saved in the `clean_files` directory
   - Final clean data saved as `clean_files/final_clean_data.csv`

2. **Garbage Data** (rows with missing or invalid data):
   - Saved in the `garbage_files` directory
   - Final garbage data saved as `garbage_files/final_garbage_data.csv`

## Process Flow

1. The script reads the input CSV in chunks.
2. For each chunk:
   - Handles missing data
   - Removes duplicates
   - Converts data types
   - Handles outliers
   - Standardizes data
   - Performs specific validations (e.g., email addresses)
3. Separates clean and garbage data
4. Saves intermediate results for each chunk
5. Concatenates all processed chunks
6. Saves final clean and garbage datasets

## Logging

The script logs its activities to `data_processing.log`, including:
- Processing start and completion for each chunk
- Missing value counts
- Any errors or exceptions encountered

## Data Fields

The script is currently set up to handle the following fields:

- VIN
- Name
- ID Number
- Gender
- Mobile Phone
- Email
- Province
- City
- Address
- Postal Code
- Date of Birth
- Industry
- Monthly Salary
- Marital Status
- Education
- Brand
- Car Series
- Car Model
- Configuration
- Color
- Engine Number

Note: These fields can be easily modified to suit different datasets by updating the `new_headers` list in the script.

## Customization

- Adjust the `chunk_size` variable to optimize performance based on your system's memory.
- Modify the `new_headers` list to match your dataset's structure.
- Add or modify data cleaning and validation steps in the `process_chunk` function as needed.
- Update the data type conversions, outlier handling, and standardization steps to fit your specific data requirements.

## Important Considerations

- Ensure you have sufficient disk space to store intermediate and final output files.
- The script assumes certain column names (e.g., 'email', 'salary'). Adjust these according to your dataset's structure.
- Back up your original data before running the script.
- Review and modify the validation and cleaning steps to ensure they're appropriate for your specific dataset.

## Note on Large Datasets

This script is designed to handle large datasets by processing them in chunks. This approach helps manage memory usage efficiently, allowing for the processing of datasets that might not fit into memory all at once.

## Extensibility

The script can be easily extended to include additional data cleaning and processing steps. Some possibilities include:
- Implementing more sophisticated outlier detection methods
- Adding data normalization or scaling steps
- Incorporating feature engineering
- Implementing more complex data validation rules

## Error Handling

The script includes basic error handling and logging. For production use, you may want to enhance the error handling to deal with specific issues that could arise with your data.
