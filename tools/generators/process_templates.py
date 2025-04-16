#!/usr/bin/env python3
# process_templates.py
# A more sophisticated template processor for converting the .txt templates to JSON-RPC files

import os
import sys
import json
import re
import argparse
import time
from datetime import datetime

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Process template files into JSON-RPC compliant files')
    parser.add_argument('--category', help='Process only the specified category')
    parser.add_argument('--output-dir', default='./json', help='Specify output directory (default: ./json)')
    parser.add_argument('--base-dir', default='.', help='Base directory containing templates (default: current dir)')
    parser.add_argument('--timestamp', action='store_true', help='Add timestamp to JSON IDs')
    return parser.parse_args()

def extract_sections(file_content):
    """Extract template and data sections from file content"""
    template_match = re.search(r'# TEMPLATE-START\n(.*?)# TEMPLATE-END', file_content, re.DOTALL)
    data_match = re.search(r'# ITEM-DATA-START\n(.*?)# ITEM-DATA-END', file_content, re.DOTALL)
    
    if not template_match:
        raise ValueError("Template section not found. Check for # TEMPLATE-START and # TEMPLATE-END markers.")
    if not data_match:
        raise ValueError("Data section not found. Check for # ITEM-DATA-START and # ITEM-DATA-END markers.")
    
    template = template_match.group(1)
    data = data_match.group(1)
    
    return template, data

def parse_data_section(data_section):
    """Parse the data section into a structured format"""
    # Split by empty lines followed by a line starting with #
    items = re.split(r'\n\s*\n\s*#\s+', data_section)
    parsed_items = []
    
    for item in items:
        if not item.strip():
            continue
            
        # Get the header if present (line starting with #)
        header_match = re.match(r'#\s+(.*?)\n', item)
        header = header_match.group(1) if header_match else None
        
        # If there was a header, remove it from the item text
        if header_match:
            item = item[header_match.end():]
        
        # Parse key-value pairs
        item_data = {'_header': header}
        for line in item.split('\n'):
            line = line.strip()
            if not line:
                continue
                
            # Check if it's a key-value pair
            kv_match = re.match(r'([^:]+?):\s*(.*)', line)
            if kv_match:
                key = kv_match.group(1).strip()
                value = kv_match.group(2).strip()
                item_data[key] = value
        
        parsed_items.append(item_data)
    
    return parsed_items

def extract_template_items(template):
    """Extract item templates from the main template"""
    items = {}
    
    # Find all sections with START/END markers
    for marker in ['FORMAT-ITEM', 'DEVICE-ITEM', 'STANDARD-ITEM', 'CATEGORY-ITEM', 'RATIO-ITEM', 'RESOLUTION-ITEM', 'ERA-ITEM']:
        start_marker = f'# {marker}-START'
        end_marker = f'# {marker}-END'
        
        pattern = f'{re.escape(start_marker)}\n(.*?){re.escape(end_marker)}'
        match = re.search(pattern, template, re.DOTALL)
        
        if match:
            items[marker] = match.group(1)
    
    return items

def fill_template(template, template_items, parsed_data, args):
    """Fill the template with data and return JSON string"""
    # Replace timestamp placeholder if present
    timestamp = int(time.time())
    template = template.replace('{{timestamp}}', str(timestamp))
    
    # Process the template based on its structure
    # This is a simplified implementation and would need to be expanded
    # for more complex template structures
    
    result = template
    
    # Replace data items in the template
    # This is a very basic implementation and would need more sophisticated parsing
    for key, value in parsed_data[0].items():
        if key != '_header':
            placeholder = f'{{{{{key}}}}}'
            result = result.replace(placeholder, value)
    
    # Try to parse the result as JSON to validate it
    try:
        json_obj = json.loads(result)
        # Return pretty-printed JSON
        return json.dumps(json_obj, indent=2)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON result: {e}")
        print("Raw result:")
        print(result)
        raise

def process_template_file(template_file, output_file, args):
    """Process a single template file"""
    print(f"Processing {template_file} -> {output_file}")
    
    with open(template_file, 'r') as f:
        file_content = f.read()
    
    try:
        template, data = extract_sections(file_content)
        parsed_data = parse_data_section(data)
        template_items = extract_template_items(template)
        
        json_output = fill_template(template, template_items, parsed_data, args)
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'w') as f:
            f.write(json_output)
        
        print(f"Created JSON file: {output_file}")
        
    except Exception as e:
        print(f"Error processing {template_file}: {e}")
        return False
    
    return True

def find_template_files(base_dir, category=None):
    """Find all template files matching the category filter"""
    template_files = []
    
    if category:
        category_path = os.path.join(base_dir, category)
        if os.path.isdir(category_path):
            for root, _, files in os.walk(category_path):
                for file in files:
                    if file.endswith('.txt'):
                        template_files.append(os.path.join(root, file))
        else:
            print(f"Category directory not found: {category}")
    else:
        for root, _, files in os.walk(base_dir):
            for file in files:
                if file.endswith('.txt'):
                    template_files.append(os.path.join(root, file))
    
    return template_files

def main():
    args = parse_args()
    
    base_dir = args.base_dir
    output_dir = args.output_dir
    
    # Find template files
    if args.category:
        print(f"Processing category: {args.category}")
        template_files = find_template_files(base_dir, args.category)
    else:
        print("Processing all template files")
        template_files = find_template_files(base_dir)
    
    success_count = 0
    error_count = 0
    
    for template_file in template_files:
        # Skip files from the output directory or scripts directory
        if output_dir in template_file or '/scripts/' in template_file:
            continue
            
        # Determine output file path
        rel_path = os.path.relpath(template_file, base_dir)
        output_file = os.path.join(output_dir, os.path.splitext(rel_path)[0] + '.json')
        
        # Process the template
        if process_template_file(template_file, output_file, args):
            success_count += 1
        else:
            error_count += 1
    
    print(f"Processing complete! Processed {success_count} files with {error_count} errors.")

if __name__ == "__main__":
    main()
