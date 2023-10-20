import pandas as pd
from App.csvFileLocation import csv_file

# Specify the date format in  CSV
date_format = '%d/%m/%Y'

# Load only a subset of rows as the initial data
initial_rows = 15000

df = pd.read_csv(csv_file, parse_dates=['OFFENCE_MONTH'], date_format=date_format, low_memory=False, nrows=initial_rows, dtype={
    'OFFENCE_FINYEAR': str,
    'OFFENCE_CODE': int,
    'OFFENCE_DESC': str,
    'LEGISLATION': str,
    'SECTION_CLAUSE': str,
    'FACE_VALUE': float,
    'CAMERA_IND': str,
    'CAMERA_TYPE': str,
    'LOCATION_CODE': str,
    'LOCATION_DETAILS': str,
    'SCHOOL_ZONE_IND': str,
    'SPEED_BAND': str,
    'SPEED_IND': str,
    'POINT_TO_POINT_IND': str,
    'RED_LIGHT_CAMERA_IND': str,
    'SPEED_CAMERA_IND': str,
    'SEATBELT_IND': str,
    'MOBILE_PHONE_IND': str,
    'PARKING_IND': str,
    'CINS_IND': str,
    'FOOD_IND': str,
    'BICYCLE_TOY_ETC_IND': str,
    'TOTAL_NUMBER': int,
    'TOTAL_VALUE': float
})

# Convert OFFENCE_MONTH to datetime if it's not already
df['OFFENCE_MONTH'] = pd.to_datetime(df['OFFENCE_MONTH'], format='%Y-%m-%d')

# Extract the starting year from OFFENCE_FINYEAR
df['OFFENCE_FINYEAR'] = df['OFFENCE_FINYEAR'].str.split('-').str[0]

# Replace NaN values with "nill" in all columns
df.fillna("no record", inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# # Save the cleaned data to a new CSV file
df.to_csv('cleaned_data.csv', index=False)

print("Data cleaning and arrangement complete. Cleaned data saved as 'cleaned_data.csv'.")


