import requests
from bs4 import BeautifulSoup
import pandas as pd

# make an HTTP GET request to the webpage
url = 'https://www.travismathew.com'
response = requests.get(url)

# parse the HTML content of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# extract all the links
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))


df = pd.DataFrame(links, columns=['Links'])

# Create an Excel writer using openpyxl
writer = pd.ExcelWriter('linkx.xlsx', engine='openpyxl')

# Write the DataFrame to the Excel file
df.to_excel(writer, index=False)

# Save the Excel file
writer.save()

# Read the Excel file
df = pd.read_excel('linkx.xlsx', usecols=[0])

# Iterate through the DataFrame to check the content of each row
for i in range(df.shape[0]):
    # Check if the row starts with "/"
    if str(df.iat[i,0]).startswith("/"):
        # Concatenate "www.travismathew.com" before the row content
        df.iat[i, 0] = "www.travismathew.com" + df.iat[i, 0]

# Create an Excel writer using openpyxl
writer = pd.ExcelWriter('linkx.xlsx', engine='openpyxl')

# Write the DataFrame to the Excel file
df.to_excel(writer, index=False)

# Save the Excel file
writer.save()


######################


# Read the Excel file
df = pd.read_excel("linkx.xlsx", usecols=[0])

# Create a new DataFrame to store the filtered values
final_df = pd.DataFrame(columns=["URL"])

# Iterate through the DataFrame to check the content of each row
for i in range(df.shape[0]):
    # Get the URL from the first column
    url = str(df.iat[i, 0])
    if (url.startswith("www.") or url.startswith('https') or url.startswith('http')) and str(url) != 'nan': # check if cell is not empty
        # Append the URL to the final_df
        final_df = final_df.append({"URL": url}, ignore_index=True)

# Create an Excel writer using openpyxl
writer = pd.ExcelWriter('final_list.xlsx', engine='openpyxl')

# Write the DataFrame to the Excel file
final_df.to_excel(writer, index=False)

# Save the Excel file
writer.save()

####################

# Read the Excel file
df = pd.read_excel("final_list.xlsx")

# Add a new column to store the status
df["Status"] = ""

# Iterate through the DataFrame to check the content of each row
for i in range(df.shape[0]):
    # Get the URL from the first column
    url = df.iat[i, 0]

    if url[-1] == "/":
        url = url[:-1]

    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(url)
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@')

    try:

        # Make a GET request to the URL
        response = requests.get(url, timeout=1)
        response.raise_for_status()
    except:
        pass

    # Check the status code
    if response.status_code == 200:
        # Update the second column with "UP"
        df.iat[i, 1] = response.status_code



    else:
        # Update the second column with "DOWN"
        df.iat[i, 1] = response.status_code



# Create an Excel writer using openpyxl
writer = pd.ExcelWriter('final_list.xlsx', engine='openpyxl')

# Write the DataFrame to the Excel file
df.to_excel(writer, index=False)

# Save the Excel file
writer.save()
