"""
R004_IMLS_OADS__
|
convert_pdf_using_grobid.py
Created on Thu Nov  7 02:36:53 2024
@author: Rochana Obadage
"""

import os
import requests
import time

# Grobid API URL (Change this if you use a different Grobid instance)
GROBID_URL = "https://kermitt2-grobid.hf.space/api/processFulltextDocument" 

# Folder paths
input_pdf_folder = "data/pdf"  # Folder containing PDFs
output_xml_folder = "data/xml"  # Folder to save extracted XML
os.makedirs(output_xml_folder, exist_ok=True)  # Ensure output folder exists

# Function to send PDF to Grobid API and save XML response
def process_pdf(pdf_path, output_folder, count):
    with open(pdf_path, "rb") as pdf_file:
        files = {"input": pdf_file}
        response = requests.post(GROBID_URL, files=files, params={"includeRawCitations": "true"})
        
        if response.status_code == 200:
            xml_output_path = os.path.join(output_folder, os.path.basename(pdf_path).replace(".pdf", ".xml"))
            with open(xml_output_path, "w", encoding="utf-8") as xml_file:
                xml_file.write(response.text)
            print(f"{count} Converted: {pdf_path} -> {xml_output_path}")
        else:
            print(f"Failed to process {pdf_path}. Status code: {response.status_code}")

# Iterate over all PDFs in the folder and process them
count = 1
for pdf_file in os.listdir(input_pdf_folder):
    if count%10 ==0:
        time.sleep(30)
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(input_pdf_folder, pdf_file)
        process_pdf(pdf_path, output_xml_folder, count)
        count+=1

print("PDF to XML conversion completed.")
