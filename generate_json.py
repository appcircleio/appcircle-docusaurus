import os
import json
import frontmatter
from pathlib import Path
from collections import defaultdict

source_dir = "flattened_docs"
output_dir = "json_docs"
mapping_file = "file_mapping.json"

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Load file mapping
file_mapping = {}
if os.path.exists(mapping_file):
    with open(mapping_file, 'r', encoding='utf-8') as f:
        file_mapping = json.load(f)

# Dictionary to store content by main section
sections = defaultdict(list)

def get_root_section(filename):
    # First, find all root-level index files to determine main sections
    index_files = [f for f in os.listdir(source_dir) if f.endswith("-index.md")]
    root_sections = []
    
    # Extract only root-level sections (those without further dashes except for special cases)
    for idx_file in index_files:
        section = idx_file.replace("-index.md", "")
        parts = section.split("-")
        
        # Handle special cases like 'self-hosted-appcircle'
        if parts[0] in ["self", "my"]:
            if len(parts) == 3 and parts[0] == "self" and parts[1] == "hosted":
                root_sections.append(section)
        elif len(parts) == 1:  # Regular root sections like 'account', 'build', etc.
            root_sections.append(section)
    
    # Find which root section this file belongs to
    for section in root_sections:
        if filename.startswith(section):
            return section
            
    # Special case for self-hosted-appcircle
    if filename.startswith("self-hosted"):
        return "self-hosted-appcircle"
        
    # Fallback: use the first part of the filename
    parts = filename.split("-")
    return parts[0]

def generate_url_from_original_path(original_path):
    """Generate Docusaurus URL from original file path"""
    # Remove file extension and convert to URL path
    url_path = original_path.replace(".md", "").replace(".mdx", "").replace("\\", "/")
    
    # Handle index files - remove /index from the end
    if url_path.endswith("/index"):
        url_path = url_path.replace("/index", "")
        
    # Handle root index file
    if url_path == "index" or url_path == "":
        url_path = ""
    
    # Construct full URL
    base_url = "https://docs.appcircle.io"
    if url_path:
        return f"{base_url}/{url_path}"
    else:
        return base_url

# Process all MD files
for file in os.listdir(source_dir):
    if not file.endswith((".md", ".mdx")):
        continue
        
    file_path = os.path.join(source_dir, file)
    
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Parse frontmatter and content
        post = frontmatter.loads(content)
        
        # Get original path from mapping and generate URL
        original_path = file_mapping.get(file, "")
        doc_url = generate_url_from_original_path(original_path) if original_path else f"https://docs.appcircle.io/{file.replace('.md', '').replace('.mdx', '')}"
        
        # Create document object
        doc = {
            "id": file.replace(".md", "").replace(".mdx", ""),
            "title": post.get("title", file),
            "content": post.content,
            "url": doc_url,
            "original_path": original_path,
            "metadata": dict(post.metadata)
        }
        
        # Determine the root section for this file
        main_section = get_root_section(file)
        sections[main_section].append(doc)
        
    except Exception as e:
        print(f"Error processing {file}: {str(e)}")

# Write JSON files
for section, documents in sections.items():
    output_file = os.path.join(output_dir, f"{section}.json")
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                "section": section,
                "documents": documents
            }, f, indent=2, ensure_ascii=False)
        print(f"Created {output_file}")
    except Exception as e:
        print(f"Error writing {output_file}: {str(e)}")
