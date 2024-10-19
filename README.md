README for Data Processing Script with Data Cleaning, Chunking, and Translating
Overview
This Python script is designed for processing large datasets in chunks, performing data cleaning, validation, and translation of column headers. The script reads the input file in chunks to handle memory constraints, cleans and validates the data, separates valid "clean" data from "garbage" data (i.e., rows with missing or invalid entries), and saves both cleaned and garbage data into separate directories. It also translates the column headers into English if required.

Features:
Chunk Processing: Handles large datasets by reading and processing the CSV file in manageable chunks.
Data Cleaning:
Handles missing values by separating invalid rows.
Removes duplicate rows.
Converts data types (e.g., age and date columns) as needed.
Detects and removes outliers (e.g., from the salary column).
Data Translation: Translates the column headers from another language to English using a custom list.
Email Validation: Uses regex to validate email addresses in the email column.
Logging: Creates detailed logs for each step in the process, including missing values, outliers, and progress for each chunk.
File Paths:
Input File: The input CSV dataset is expected at ./760k-Car-Owners-Nationwide-China-csv-2020.csv.
Output Files:
Cleaned data is saved in clean_files/final_clean_data.csv.
Invalid/garbage data is saved in garbage_files/final_garbage_data.csv.
Key Steps:
Chunk Processing:

The dataset is processed in chunks of 250,000 rows, which allows the script to handle large datasets without running into memory issues.
Data Cleaning:

Missing Data: Rows with missing values are separated as garbage data. This helps maintain the integrity of the cleaned data.
Duplicate Removal: Duplicates are removed within each chunk to ensure data consistency.
Data Type Conversion: The age column is converted to numeric data type, and date_column is converted to a datetime format.
Outlier Detection: Outliers in the salary column are identified and removed based on the Interquartile Range (IQR) method.
Standardization: The name column is standardized to lowercase and stripped of leading and trailing spaces.
Email Validation:

The email column is validated using a regex pattern. Invalid email addresses are flagged or discarded.
Data Translation:

The script replaces the original column headers with a predefined set of translated headers in English:
'VIN', 'Name', 'ID Number', 'Gender', 'Mobile Phone', 'Email', 'Province', 'City', 'Address', 'Postal Code', 'Date of Birth', 'Industry', 'Monthly Salary', 'Marital Status', 'Education', 'Brand', 'Car Series', 'Car Model', 'Configuration', 'Color', 'Engine Number'.
Final Output:

After all chunks are processed, the clean and garbage data from all chunks are concatenated into two separate files: one for the cleaned data and one for the garbage data.
Logging:

The script logs details about missing values, outliers, duplicates, and the progress of each chunk. Logs are saved to data_processing.log.
Custom Headers:
The script replaces the existing headers with the following translated headers:

'VIN', 'Name', 'ID Number', 'Gender', 'Mobile Phone', 'Email', 'Province', 'City', 'Address', 'Postal Code', 'Date of Birth', 'Industry', 'Monthly Salary', 'Marital Status', 'Education', 'Brand', 'Car Series', 'Car Model', 'Configuration', 'Color', 'Engine Number'.
Requirements:
Python 3.x
Libraries:
pandas
os
logging
re
Install the required Python libraries via pip:

bash
Copy code
pip install pandas
How to Run:
Place the input CSV file at ./760k-Car-Owners-Nationwide-China-csv-2020.csv.
Run the script:
bash
Copy code
python data_processing.py
The cleaned data will be saved to clean_files/final_clean_data.csv, and the garbage data will be saved to garbage_files/final_garbage_data.csv.
A log file will be generated and saved as data_processing.log.
Output:
Clean Data: The final cleaned dataset will contain rows without missing values or invalid data.
Garbage Data: The final garbage dataset will include rows with missing or invalid data for further review.
Customization:
Chunk Size: You can change the chunk size for processing large files by modifying the chunk_size variable.
Custom Headers: The list of new headers in English can be modified to suit your specific dataset by adjusting the new_headers list.
Translation: The current script uses predefined translations for the headers. If you need to translate additional columns or text, you can integrate the Deep Translator library or another translation service.
Logging:
Log File: A detailed log is saved at data_processing.log. This log includes:
The number of missing values in each chunk.
Notifications of when chunks start and finish processing.
Details of data transformations such as duplicate removal and outlier filteri
