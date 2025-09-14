import os
import json
import frontmatter
from collections import defaultdict

source_dir = "flattened_docs"
output_dir = "structured_docs"
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

def get_main_section(original_path):
    """Extract the main section from original file path"""
    if not original_path:
        return "misc"
    
    # Get the first part of the path
    parts = original_path.split("/")
    first_part = parts[0]
    
    # Handle root-level files (no slash in path)
    if len(parts) == 1:
        if first_part.startswith("_"):
            return "components"  # All underscore files go to components
        elif first_part == "release-notes.md":
            return "general"
        elif first_part in ["intro.md", "getting-started-with-appcircle.md"]:
            return "general"
        else:
            return "general"  # Other root files go to general
    
    # Handle directory-based files
    if first_part.startswith("_"):
        return "components"
    elif first_part == "self-hosted-appcircle":
        return "self-hosted"
    else:
        return first_part

def clean_section_name(section_name):
    """Clean up section names for better file naming"""
    name_mapping = {
        "self-hosted": "self-hosted",
        "build": "build", 
        "publish-module": "publish",
        "publish-integrations": "publish-integrations",
        "testing-distribution": "testing",
        "enterprise-app-store": "enterprise",
        "signing-identities": "signing",
        "environment-variables": "environment",
        "continuous-testing": "testing",
        "appcircle-api-and-cli": "api-cli",
        "best-practices": "best-practices",
        "components": "components",
        "general": "general",
        "workflows": "workflows",
        "versioning": "versioning",
        "infrastructure": "infrastructure",
        "marketplace": "marketplace",
        "code-push": "code-push"
    }
    return name_mapping.get(section_name, section_name)

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
            "title": post.get("title", file.replace(".md", "").replace(".mdx", "")),
            "description": post.get("description", ""),
            "content": post.content,
            "url": doc_url,
            "original_path": original_path,
            "tags": post.get("tags", []),
            "sidebar_position": post.get("sidebar_position", None),
            "metadata": dict(post.metadata)
        }
        
        # Determine the main section for this file
        main_section = get_main_section(original_path)
        sections[main_section].append(doc)
        
    except Exception as e:
        print(f"Error processing {file}: {str(e)}")

# Write consolidated JSON files
for section, documents in sections.items():
    # Sort documents by their original path for better organization
    documents.sort(key=lambda x: x.get("original_path", ""))
    
    # Clean section name for filename
    clean_name = clean_section_name(section)
    output_file = os.path.join(output_dir, f"{clean_name}.json")
    
    # Create the consolidated structure
    consolidated_data = {
        "section": clean_name,
        "section_title": section.replace("-", " ").title(),
        "total_documents": len(documents),
        "documents": documents,
        "generated_at": "2025-08-19"  # You can make this dynamic if needed
    }
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(consolidated_data, f, indent=2, ensure_ascii=False)
        print(f"✅ Created {output_file} with {len(documents)} documents")
    except Exception as e:
        print(f"❌ Error writing {output_file}: {str(e)}")

print(f"\n🎉 Consolidated JSON files generated in: {output_dir}/")
print(f"📊 Total sections processed: {len(sections)}")