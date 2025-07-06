#!/bin/bash

# Path to the parent directory containing subfolders with LaTeX sources
parent_dir="data/latex"

# Base output directory for HTML files
output_base_dir="data/html"
mkdir -p "$output_base_dir"

# Iterate through each folder in the parent directory
for folder in "$parent_dir"/*; do
    if [ -d "$folder" ]; then
        echo "Processing folder: $folder"
        
        # Find the .bbl file in the folder
        bbl_file=$(find "$folder" -type f -name "*.bbl" | head -n 1)
        
        if [ -n "$bbl_file" ]; then
            # Get the base name of the .bbl file (without extension)
            base_name=$(basename "$bbl_file" .bbl)

            # Construct the corresponding .tex file path
            main_tex_file="$folder/$base_name.tex"
            
            if [ -f "$main_tex_file" ]; then
                echo "Found main tex file: $main_tex_file"

                base_name_folder=$(basename "$folder")
                
                # Create an output directory for this article
                article_output_dir="$output_base_dir/$base_name_folder"
                mkdir -p "$article_output_dir"

                # Generate output file paths
                xml_file="$article_output_dir/$base_name.xml"
                html_file="$article_output_dir/$base_name.html"

                # Convert LaTeX to LaTeXML
                latexml --dest="$xml_file" "$main_tex_file"

                # Convert LaTeXML XML to HTML
                latexmlpost --dest="$html_file" "$xml_file"

                echo "Converted $main_tex_file to $html_file"
            else
                echo "No corresponding .tex file found for $bbl_file"
            fi
        else
            echo "No .bbl file found in $folder"
        fi
    fi
done
