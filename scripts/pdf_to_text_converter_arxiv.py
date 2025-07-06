"""
R004_IMLS_OADS__
|
pdf_to_text_converter_arxiv.py
Created on Thu Oct 24 18:34:20 2024
@author: Rochana Obadage
"""

import pymupdf
import os


def convert_pdf_to_text(pdf_path, text_path):
    """
    Convert a PDF file to a text file.

    Args:
        pdf_path (str): Path to the PDF file.
        text_path (str): Path where the text file will be saved.
    """
    try:
        # Open the PDF file
        pdf_document = pymupdf.open(pdf_path)
    except Exception as e:
        print(f"Error opening PDF file '{pdf_path}': {e}")
        return  # Exit the function if the PDF cannot be opened

    text_content = ""

    try:
        # Iterate through each page in the PDF
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            text_content += page.get_text() + "\n"  # Append the text of each page
    except Exception as e:
        print(f"Error reading pages from PDF file '{pdf_path}': {e}")
        pdf_document.close()  # Ensure the PDF is closed if an error occurs
        return  # Exit the function if an error occurs while reading

    pdf_document.close()

    try:
        # Write the extracted text to the text file
        with open(text_path, 'w', encoding='utf-8') as text_file:
            text_file.write(text_content)
    except Exception as e:
        print(f"Error writing to text file '{text_path}': {e}")


def convert_all_pdfs_in_directory(pdf_directory_path):
    """
    Convert all PDF files in a directory to text files, saving each text file in the 'converted' folder
    while preserving the subdirectory structure.

    Args:
        pdf_directory_path (str): Path to the root directory containing PDF files in nested directories.
    """
    converted_root = "/data/text/"
    os.makedirs(converted_root, exist_ok=True)

    count = 0
    for root, _, files in os.walk(pdf_directory_path):
        # Determine the relative path of the current directory to the root directory
        relative_path = os.path.relpath(root, pdf_directory_path)
        converted_subdirectory = os.path.join(converted_root, relative_path)

        # Check if the directory already exists in arxiv-txt
        if os.path.exists(converted_subdirectory):
            print(f"Skipping {root} as {converted_subdirectory} already exists.")
            continue

        # Create the corresponding subdirectory structure in the 'converted' folder
        os.makedirs(converted_subdirectory, exist_ok=True)

        for file_name in files:
            if file_name.lower().endswith(".pdf"):
                pdf_file_path = os.path.join(root, file_name)
                text_file_name = file_name.replace(".pdf", ".txt")
                text_file_path = os.path.join(converted_subdirectory, text_file_name)

                # Convert the PDF file to a text file
                convert_pdf_to_text(pdf_file_path, text_file_path)
                count += 1
                print(f"{count} Converted {pdf_file_path} to {text_file_path}")

# Path to the root directory containing PDF files in nested directories
pdf_directory_path = "/data/pdf"

# Convert all PDFs in the specified directory to text files
convert_all_pdfs_in_directory(pdf_directory_path)
