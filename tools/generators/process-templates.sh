#!/bin/bash
# process-templates.sh
# Script to process template files into JSON format

# Print script usage
print_usage() {
  echo "Usage: $0 [OPTIONS]"
  echo "Process template files into JSON-RPC compliant files"
  echo ""
  echo "Options:"
  echo "  --category=CATEGORY   Process only the specified category"
  echo "  --output-dir=DIR      Specify output directory (default: ./json)"
  echo "  --help                Display this help message"
  echo ""
  echo "Examples:"
  echo "  $0                              # Process all templates"
  echo "  $0 --category=cinema           # Process only cinema templates"
  echo "  $0 --output-dir=./output/json  # Output to custom directory"
}

# Initialize variables
CATEGORY=""
OUTPUT_DIR="./json"

# Parse command line arguments
for arg in "$@"; do
  case $arg in
    --category=*)
      CATEGORY="${arg#*=}"
      shift
      ;;
    --output-dir=*)
      OUTPUT_DIR="${arg#*=}"
      shift
      ;;
    --help)
      print_usage
      exit 0
      ;;
    *)
      echo "Unknown option: $arg"
      print_usage
      exit 1
      ;;
  esac
done

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Function to process a template file
process_template() {
  local template_file="$1"
  local output_file="$2"
  
  echo "Processing $template_file -> $output_file"
  
  # Extract the template section
  TEMPLATE=$(sed -n '/# TEMPLATE-START/,/# TEMPLATE-END/p' "$template_file" | sed '1d;$d')
  
  # Extract the data section
  DATA=$(sed -n '/# ITEM-DATA-START/,/# ITEM-DATA-END/p' "$template_file" | sed '1d;$d')
  
  # Process the data into the template
  # Note: This is a simplified placeholder. A real implementation would
  # need more sophisticated parsing of the data and template sections.
  
  # For now, we'll just output the template as a placeholder
  echo "$TEMPLATE" > "$output_file"
  
  echo "Created JSON file: $output_file"
  echo "Note: This is a placeholder implementation. A real parser would"
  echo "substitute the template variables with actual data values."
}

# Main processing logic
if [ -n "$CATEGORY" ]; then
  echo "Processing category: $CATEGORY"
  
  # Find template files for the specified category
  if [ -d "./$CATEGORY" ]; then
    find "./$CATEGORY" -name "*.txt" | while read template_file; do
      filename=$(basename "$template_file" .txt)
      output_file="$OUTPUT_DIR/${filename}.json"
      process_template "$template_file" "$output_file"
    done
  else
    echo "Category directory not found: $CATEGORY"
    exit 1
  fi
else
  echo "Processing all template files"
  
  # Find all template files
  find . -name "*.txt" | while read template_file; do
    dir=$(dirname "$template_file")
    filename=$(basename "$template_file" .txt)
    output_file="$OUTPUT_DIR/${dir#./}/${filename}.json"
    
    # Create output subdirectory if needed
    mkdir -p "$(dirname "$output_file")"
    
    process_template "$template_file" "$output_file"
  done
fi

echo "Processing complete!"
