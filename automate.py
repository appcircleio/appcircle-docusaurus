import os
import shutil
import frontmatter
import json
from pathlib import Path

source_dir = "docs"
output_dir = "flattened_docs"
structure_file = "docs-structure.md"
mapping_file = "file_mapping.json"

os.makedirs(output_dir, exist_ok=True)

structure_lines = ["# 📚 Documentation Structure Overview\n"]
file_mapping = {}

def slugify_path(path_parts):
    return "-".join(path_parts).replace(" ", "-")

for root, _, files in os.walk(source_dir):
    rel_path = Path(root).relative_to(source_dir)
    folder_parts = list(rel_path.parts)
    
    if folder_parts:
        structure_lines.append(f"\n## {' / '.join(folder_parts)}")

    for file in files:
        if not file.endswith((".md", ".mdx")):
            continue

        src_file_path = os.path.join(root, file)
        path_parts = folder_parts + [file.replace(".md", "").replace(".mdx", "")]
        flat_filename = slugify_path(path_parts) + Path(file).suffix
        dst_file_path = os.path.join(output_dir, flat_filename)

        shutil.copyfile(src_file_path, dst_file_path)

        # Store the mapping between flattened filename and original path
        original_rel_path = str(Path(root).relative_to(source_dir) / file)
        file_mapping[flat_filename] = original_rel_path

        # Try to extract title from frontmatter
        try:
            with open(src_file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                title = post.get('title', path_parts[-1])
        except:
            title = path_parts[-1]

        structure_lines.append(f"- [{title}]({flat_filename})")

# Write structure file
with open(os.path.join(output_dir, structure_file), "w", encoding="utf-8") as f:
    f.write("\n".join(structure_lines))

# Write mapping file
with open(mapping_file, "w", encoding="utf-8") as f:
    json.dump(file_mapping, f, indent=2, ensure_ascii=False)

print(f"\n✅ All files flattened into: {output_dir}/")
print(f"📄 Structure index generated: {structure_file}")
print(f"🗺️  File mapping created: {mapping_file}")