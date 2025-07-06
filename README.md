# 🧾 URL Extraction Performance Across arXiv File Formats

This repository contains all data, code, and results related to our study on extracting and evaluating URLs from multi-format representations of arXiv research papers. It supports a longitudinal and format-wise analysis of URL extraction from open-access scholarly documents and includes a pilot dataset of arXiv papers across formats (PDF, LaTeX, HTML, XML, and plain text), ground truth annotations of valid and OADS-related URLs, as well as scripts and the jupyter notebook to extract, evaluate, and visualize URL extraction performance.

---

## 📂 Repository Structure

```
├── data/ # Full-text files from arXiv in multiple formats
│  ├── html/ 
│  ├── latex/ 
│  ├── pdf/ 
│  ├── text/ 
│  └── xml/ 
│
├── figures/ 
│
├── results/ 
│  ├── extracted_urls_1000_per_year.json
│  ├── extracted_urls_1000_per_year_10_samples_all_12_folders.json
│  ├── html_urls.json
│  ├── latex_urls.json
│  ├── text_urls.json
│  └── xml_urls.json
│
├── scripts/
│  ├── convert_pdf_using_grobid.py
│  ├── pdf_to_text_converter_arxiv.py
│  └── convert_latex_to_html.sh
│
├── arxiv_extracted_urls_comparison.xlsx 
├── arxiv_file_formats.ipynb
└── README.md

```

---

## 📁 Data

- The data/ folder includes the same arXiv papers in:

   - `pdf/`: original PDFs
   - `latex/`: LaTeX source files
   - `html/`: converted using LaTeXML
   - `xml/`: converted using GROBID
   - `text/`: plain text via PyMuPDF
   
- `*.json` files in `results/` contain extracted URL lists by format.
- `arxiv_extracted_urls_comparison.xlsx` summarizes format coverage and valid URL extractions.
---

## ⚙️ Key Scripts

| scripts/{File}                         | Description                                      |
|------------------------------------|--------------------------------------------------|
| `pdf_to_text_converter_arxiv.py`   | Converts PDFs to plain text using PyMuPDF       |
| `convert_pdf_using_grobid.py`      | Extracts XML from PDFs using GROBID             |
| `convert_latex_to_html.sh`         | Converts LaTeX source to HTML using LaTeXML     |

---

## 🛠️ Tools Used

- Python 3.10.16
- LaTeXML 0.8.8
- GROBID 0.8.1
- PyMuPDF 1.24.13

---
## 🚀 To reproduce the results

### 1. Clone the Repository

```bash
git clone https://github.com/lamps-lab/arxiv-urls.git
cd arxiv-urls
```

### 2. Install Requirements

- Create a virtual environment and install required packages:

    ```bash
    pip install PyMuPDF==1.24.13 lxml pylatexenc

    ```
- Install LaTeXML 0.8.8 by following the official instructions: https://math.nist.gov/~BMiller/LaTeXML/

### 3. Run the Jupyter Notebook

- `arxiv_file_formats.ipynb` – Random paper selection, Format conversion, url extraction, visualizations
---


<!-- ## 📚 Citation -->


<!-- ```bibtex

``` 
--- -->

```
Rochana R. Obadage 
Updated on: 07/06/2025

```