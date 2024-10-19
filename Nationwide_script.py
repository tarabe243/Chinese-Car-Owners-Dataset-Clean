import pandas as pd
import os
import logging
import re

# Configure logging
logging.basicConfig(filename='data_processing.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# File path to your dataset
input_file = './760k-Car-Owners-Nationwide-China-csv-2020.csv'
output_file_clean = 'clean_files/final_clean_data.csv'
output_file_garbage = 'garbage_files/final_garbage_data.csv'

# Directory for saving garbage and clean files
garbage_dir = 'garbage_files'
clean_dir = 'clean_files'

# Ensure directories exist
os.makedirs(garbage_dir, exist_ok=True)
os.makedirs(clean_dir, exist_ok=True)

# Chunk size for processing large files
chunk_size = 250000

# Custom list of headers to replace the existing headers
new_headers = [
    'VIN', 'Name', 'ID Number', 'Gender', 'Mobile Phone', 'Email', 'Province', 
    'City', 'Address', 'Postal Code', 'Date of Birth', 'Industry', 'Monthly Salary', 
    'Marital Status', 'Education', 'Brand', 'Car Series', 'Car Model', 
    'Configuration', 'Color', 'Engine Number'
]

# Function to validate emails using regex (example for 'email' column)
def validate_email(email):
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if isinstance(email, str):
        return bool(re.match(email_pattern, email))
    return False

# Function to process chunks
def process_chunk(chunk, chunk_number):
    logging.info(f"Processing chunk {chunk_number}...")

    # Step 1: Handling Missing Data
    missing_vals = chunk.isnull().sum()
    logging.info(f"Missing values in chunk {chunk_number}: {missing_vals.to_dict()}")

    # Separate garbage rows (rows with missing or invalid data)
    garbage_chunk = chunk[chunk.isnull().any(axis=1)]
    clean_chunk = chunk.dropna()

    # Step 2: Removing Duplicates
    clean_chunk.drop_duplicates(inplace=True)

    # Step 3: Converting Data Types (example: assuming 'age' and 'date' columns exist)
    if 'age' in clean_chunk.columns:
        clean_chunk['age'] = pd.to_numeric(clean_chunk['age'], errors='coerce')
    if 'date_column' in clean_chunk.columns:
        clean_chunk['date_column'] = pd.to_datetime(clean_chunk['date_column'], errors='coerce')

    # Step 4: Handling Outliers (example: assuming 'salary' column exists)
    if 'salary' in clean_chunk.columns:
        Q1 = clean_chunk['salary'].quantile(0.25)
        Q3 = clean_chunk['salary'].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        clean_chunk = clean_chunk[(clean_chunk['salary'] >= lower_bound) & (clean_chunk['salary'] <= upper_bound)]

    # Step 5: Standardizing Data (example: 'name' column)
    if 'name' in clean_chunk.columns:
        clean_chunk['name'] = clean_chunk['name'].str.lower().str.strip()

    # Step 7: Validate Email Column (example: 'email' column)
    if 'email' in clean_chunk.columns:
        clean_chunk['valid_email'] = clean_chunk['email'].apply(validate_email)

    # Save garbage and clean files for each chunk
    garbage_chunk.to_csv(f'{garbage_dir}/garbage_chunk_{chunk_number}.csv', index=False)
    clean_chunk.to_csv(f'{clean_dir}/clean_chunk_{chunk_number}.csv', index=False)

    return garbage_chunk, clean_chunk

# Initialize lists to hold garbage and clean chunks for concatenation
all_garbage_chunks = []
all_clean_chunks = []

# Read and process the CSV file in chunks with custom headers
for chunk_number, chunk in enumerate(pd.read_csv(input_file, chunksize=chunk_size, names=new_headers, header=0)):
     garbage_chunk, clean_chunk = process_chunk(chunk, chunk_number)
all_garbage_chunks.append(garbage_chunk)
all_clean_chunks.append(clean_chunk)

# Concatenate all garbage and clean chunks into single DataFrames
final_garbage_df = pd.concat(all_garbage_chunks, ignore_index=True)
final_clean_df = pd.concat(all_clean_chunks, ignore_index=True)

# Save final garbage and clean DataFrames to CSV
final_garbage_df.to_csv(output_file_garbage, index=False)
final_clean_df.to_csv(output_file_clean, index=False)

logging.info("Data cleaning, header replacement, and chunk processing completed.")

