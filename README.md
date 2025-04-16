# Media Grids

[![JSON-RPC Compliant](https://img.shields.io/badge/JSON--RPC-2.0-green)](https://www.jsonrpc.org/specification) [![AI Assisted](https://img.shields.io/badge/AI%20Assisted-Human%20+%20Machine-ff69b4?logo=heart&logoColor=white)](https://github.com/a-Gb) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Made With Love](https://img.shields.io/badge/Made%20With-♥-red)](https://github.com/a-Gb)

A comprehensive collection of media specifications, display formats, and aspect ratios across various devices and standards.

## Overview

With the proliferation of digital devices, screen types, and media formats, keeping track of the correct specifications for design and development becomes challenging. Media Grids aims to be a single source of truth for these specifications, making it easier to:

- Design responsive interfaces
- Create properly formatted media for different platforms
- Understand the technical limitations of various display technologies
- Access historical specifications for legacy support

## Schema

All data follows a JSON-RPC 2.0 compliant schema, allowing for:
- Programmatic updates and modifications
- Multi-user contributions via RPC methods
- Versioning and change tracking
- Consistent data structure across all media types

## Structure

The repository is organized in a domain-based hierarchical structure:

```
media-grids/
├── domains/                     # Major domain categories
│   ├── display/                 # All display technologies
│   │   ├── cinema/              # Theater projection systems
│   │   ├── television/          # TV display technologies
│   │   ├── mobile/              # Mobile device displays
│   │   │   ├── phones/          # Smartphone displays
│   │   │   └── tablets/         # Tablet displays
│   │   ├── computer/            # Computer monitors
│   │   └── wearable/            # Wearable displays
│   │
│   ├── content/                 # Content creation formats
│   │   ├── film/                # Film formats and standards
│   │   ├── broadcast/           # Broadcast standards
│   │   ├── streaming/           # Streaming specifications
│   │   └── print/               # Print media formats
│   │
│   └── interactive/             # Interactive media
│       ├── gaming/              # Video game display standards
│       ├── ar-vr/               # Augmented/Virtual reality
│       └── presentation/        # Presentation formats
│
├── standards/                   # Cross-domain standards
│   ├── aspect-ratios/           # Aspect ratio definitions
│   ├── resolutions/             # Resolution specifications
│   ├── color/                   # Color specifications
│   │   ├── spaces/              # Color spaces
│   │   ├── depths/              # Color bit depths
│   │   └── gamuts/              # Color gamuts
│   └── temporal/                # Time-based standards
│       ├── frame-rates/         # Frame rate standards
│       └── refresh-rates/       # Display refresh rates
│
├── reference/                   # Reference materials
│   ├── glossary/                # Terminology definitions
│   ├── timelines/               # Historical evolution
│   └── conversions/             # Conversion tools and references
│
├── templates/                   # Template structures for data
│
└── tools/                       # Processing tools
    ├── generators/              # Generate JSON from templates
    ├── validators/              # Validate data against schemas
    └── converters/              # Convert between formats
```

## Usage

Each category contains template `.txt` files that can be processed into JSON-RPC compliant data. The template structure makes it easy to:

- Import into your design tools after processing
- Contribute new specifications through a consistent format
- Transform templates into other formats as needed
- Process templates programmatically for different applications

## Processing Templates

Templates can be converted to JSON using the included processing tools:

```bash
# Example: Process all templates into JSON
./tools/generators/process-templates.sh

# Example: Process a specific category
./tools/generators/process-templates.sh --category=domains/display/cinema
```

## Cross-Reference System

Media Grids implements a cross-reference system where related standards can reference each other, allowing for easy navigation between interconnected specifications.

## Contributing

We welcome contributions to expand the database of specifications. Please see our [CONTRIBUTING.md](CONTRIBUTING.md) guidelines for details on how to submit new specifications or corrections.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.