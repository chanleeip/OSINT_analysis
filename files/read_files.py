import pandas as pd

# Specify the file path
def get_email_ids(path):
    
    # Read the CSV file using pandas
    data = pd.read_csv(path,header=None)

    email_ids=[]
    # Print the data
    for i,j in data.iterrows():
        email_ids.append(j.iloc[0])

    return email_ids
# print(get_email_ids("/Users/admin/Desktop/Everything everywhere all at once/projects/Cybersecurity-osint/OSINT_analysis/Threat Actor Emails - Sheet1.csv"))