#!/usr/bin/env python3
"""Fix all JSON files by adding missing 'doctype' field"""

import json
from pathlib import Path

def fix_json_file(json_path):
    """Add missing doctype field to JSON file"""
    with open(json_path, 'r') as f:
        data = json.load(f)

    # Add 'doctype': 'DocType' if missing
    if 'doctype' not in data:
        # Create new dict with doctype first
        fixed_data = {'doctype': 'DocType'}
        fixed_data.update(data)

        with open(json_path, 'w') as f:
            json.dump(fixed_data, f, indent=1)

        print(f"✓ Fixed: {json_path.name}")
        return True
    return False

# Fix all doctype JSON files
doctype_dir = Path('manchipustakam/manchi_pustakam/doctype')
fixed_count = 0

for json_file in sorted(doctype_dir.rglob('*.json')):
    if fix_json_file(json_file):
        fixed_count += 1

print(f"\n✅ Fixed {fixed_count} JSON files")
