# Contributing to Media Grids

Thank you for your interest in contributing to Media Grids! This document provides guidelines for contributing to the project.

## Overview

Media Grids aims to be a comprehensive collection of media specifications, display formats, and aspect ratios across various devices and standards. By contributing, you help make this resource more valuable for designers, developers, and content creators.

## How to Contribute

### Adding New Specifications

1. **Identify the appropriate domain and category**: Determine where your new specification belongs within our hierarchical structure:
   - Is it a display technology? → `domains/display/[specific-category]`
   - Is it a content format? → `domains/content/[specific-category]`
   - Is it a cross-domain standard? → `standards/[standard-type]`

2. **Use the template format**: All specifications should be added to the `.txt` template files, following the existing format:
   - Add your data in the `ITEM-DATA` section
   - Follow the key-value pair format: `key: value`
   - Separate items with blank lines
   - Start each item with a comment header (e.g., `# IMAX 70mm`)

3. **Include comprehensive data**: Try to fill in as many fields as possible in the template, even if some information requires research

4. **Add cross-references**: Include references to related standards using their IDs (e.g., aspect ratio, color space)

5. **Verify your information**: Ensure all specifications are accurate and from reliable sources

### Template Format

Template files consist of two main sections:

1. **TEMPLATE section**: Defines the JSON-RPC structure (don't modify unless adding new properties)
2. **ITEM-DATA section**: Contains the actual specification data (add your new entries here)

Example:
```
# ITEM-DATA-START
# Academy Ratio
id: academy-ratio
name: Academy Ratio
aspect_ratio: 1.375:1
decimal_ratio: 1.375
# ... additional fields ...

# Your New Format
id: your-format-id
name: Your Format Name
aspect_ratio: X:Y
decimal_ratio: X.Y
# ... fill in all applicable fields ...
# ITEM-DATA-END
```

### Processing Templates

After adding new specifications:

1. Use the provided processing tools to generate JSON files:

```bash
# Process all templates
./tools/generators/process-templates.sh

# Process a specific category
./tools/generators/process-templates.sh --category=domains/display/cinema
```

2. Verify that the JSON output is correctly formatted and contains your new data

### Adding New Categories

If you need to add an entirely new category not covered by the existing structure:

1. Propose the new category by opening an issue first to discuss its placement
2. Follow the established naming conventions and directory structure
3. Create appropriate template files based on existing templates
4. Add relevant documentation to explain the new category

## Submitting Changes

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes following the guidelines above
4. Test by processing templates into JSON
5. Submit a pull request with a clear description of your additions or changes

## Code of Conduct

- Be respectful of other contributors
- Provide constructive feedback
- Focus on the technical accuracy of specifications
- Give proper attribution when sourcing information

## Questions?

If you have questions about contributing, please open an issue in the repository, and we'll be happy to help!

Thank you for helping to build a comprehensive media specification resource!
