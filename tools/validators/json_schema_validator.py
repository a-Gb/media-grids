#!/usr/bin/env python3
# json_schema_validator.py
# A tool to validate JSON files against their schema definitions

import os
import sys
import json
import argparse
import jsonschema
from jsonschema import validate

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Validate JSON files against their schema definitions')
    parser.add_argument('--file', help='JSON file to validate')
    parser.add_argument('--dir', help='Directory of JSON files to validate')
    parser.add_argument('--schema', help='Schema file to validate against')
    parser.add_argument('--schema-dir', default='./schemas', help='Directory containing schema files')
    return parser.parse_args()

def load_schema(schema_file):
    """Load a JSON schema from a file"""
    try:
        with open(schema_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading schema file {schema_file}: {e}")
        return None

def validate_json(json_file, schema):
    """Validate a JSON file against a schema"""
    try:
        with open(json_file, 'r') as f:
            json_data = json.load(f)
        
        validate(instance=json_data, schema=schema)
        print(f"✓ {json_file} is valid")
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"✗ {json_file} is invalid:")
        print(f"  Error: {e.message}")
        print(f"  Path: {'.'.join(str(x) for x in e.path)}")
        return False
    except Exception as e:
        print(f"✗ Error validating {json_file}: {e}")
        return False

def determine_schema_for_file(json_file, schema_dir):
    """Determine which schema to use for a given JSON file"""
    # Load the JSON file to check its category
    try:
        with open(json_file, 'r') as f:
            json_data = json.load(f)
        
        # Check if it's a JSON-RPC 2.0 compliant file
        if json_data.get('jsonrpc') == '2.0' and 'params' in json_data:
            category = json_data['params'].get('category', '')
            
            # Map category to schema file
            category_parts = category.split('.')
            main_category = category_parts[0]
            
            # Build potential schema paths
            schema_paths = [
                os.path.join(schema_dir, f"{main_category}-schema.json"),
                os.path.join(schema_dir, f"{category.replace('.', '-')}-schema.json"),
                os.path.join(schema_dir, "default-schema.json")
            ]
            
            # Return the first schema that exists
            for schema_path in schema_paths:
                if os.path.exists(schema_path):
                    return schema_path
                    
            # If no specific schema found, use the generic one
            return os.path.join(schema_dir, "media-grids-schema.json")
        else:
            # Not a JSON-RPC file, use generic schema
            return os.path.join(schema_dir, "generic-schema.json")
    except Exception as e:
        print(f"Error determining schema for {json_file}: {e}")
        return os.path.join(schema_dir, "media-grids-schema.json")

def validate_directory(directory, schema_dir):
    """Validate all JSON files in a directory"""
    success_count = 0
    error_count = 0
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_file = os.path.join(root, file)
                schema_file = determine_schema_for_file(json_file, schema_dir)
                
                if os.path.exists(schema_file):
                    schema = load_schema(schema_file)
                    if schema:
                        if validate_json(json_file, schema):
                            success_count += 1
                        else:
                            error_count += 1
                else:
                    print(f"✗ No schema found for {json_file}")
                    error_count += 1
    
    print(f"\nValidation complete: {success_count} files valid, {error_count} files invalid")
    return error_count == 0

def main():
    args = parse_args()
    
    if args.file and args.schema:
        # Validate a single file against a specific schema
        schema = load_schema(args.schema)
        if schema:
            success = validate_json(args.file, schema)
            sys.exit(0 if success else 1)
    elif args.file:
        # Validate a single file against an automatically determined schema
        schema_file = determine_schema_for_file(args.file, args.schema_dir)
        if os.path.exists(schema_file):
            schema = load_schema(schema_file)
            if schema:
                success = validate_json(args.file, schema)
                sys.exit(0 if success else 1)
        else:
            print(f"✗ No schema found for {args.file}")
            sys.exit(1)
    elif args.dir:
        # Validate all JSON files in a directory
        success = validate_directory(args.dir, args.schema_dir)
        sys.exit(0 if success else 1)
    else:
        print("Error: Either --file or --dir must be specified")
        sys.exit(1)

if __name__ == "__main__":
    main()
