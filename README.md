# 🧾 URL Extraction Performance Across arXiv File Formats

This repository contains all data, code, and results related to our study on extracting and evaluating URLs from multi-format representations of arXiv research papers. It supports a longitudinal and format-wise analysis of URL extraction from open-access scholarly documents and includes a pilot dataset of arXiv papers across formats (PDF, LaTeX, HTML, XML, and plain text), ground truth annotations of valid and OADS-related URLs, as well as scripts and notebooks to extract, evaluate, and visualize URL extraction performance.

---

## 📂 Repository Structure

```
├───data
│   ├───html
│   ├───latex
│   ├───pdf
│   ├───text
│   └───xml
│
├───figures
│
├───scripts
│   ├───convert_pdf_using_grobid.py
│   └───pdf_to_text_converter_arxiv.py
│
├───arxiv_extracted_urls_comparison.xlsx
└───README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/lamps-lab/arxiv-urls.git
cd arxiv-urls
```

### 2. Install Requirements

- Create a virtual environment and install required packages:

    ```bash
    pip install PyMuPDF==1.24.13

    ```
- Install LaTeXML 0.8.8 by following the official instructions: https://math.nist.gov/~BMiller/LaTeXML/

### 3. Run Jupyter Notebooks

- `arxiv_file_formats.ipynb` – Format conversion, url extraction, visualizations

---

## 📁 Data

The data/ folder includes the same arXiv papers in:

- `pdf/`: original PDFs
- `latex/`: LaTeX source files
- `html/`: converted using LaTeXML
- `xml/`: converted using GROBID
- `text/`: plain text via PyMuPDF

---

## 🛠️ Tools Used

- Python 3.10+
- LaTeXML 0.8.8
- GROBID 0.8.1
- PyMuPDF 1.24.13

---


<!-- ## 📚 Citation -->


<!-- ```bibtex

``` 
--- -->

```
Rochana R. Obadage 
Updated on: 07/04/2025

```