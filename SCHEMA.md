# Media Grids JSON-RPC 2.0 Schema Reference

This document provides the reference schema for all JSON-RPC 2.0 compliant files in the Media Grids project.

## Base Schema

All data files should follow this basic structure:

```json
{
  "jsonrpc": "2.0",
  "method": "media.get",
  "params": {
    "category": "category-name",
    "version": "1.0",
    "data": [...]
  },
  "id": "unique-identifier"
}
```

## Schema Properties

| Property | Type | Description |
|----------|------|-------------|
| jsonrpc | string | Must be "2.0" |
| method | string | One of: "media.get", "media.update", "media.add", "media.delete" |
| params | object | Container for all data parameters |
| params.category | string | The media category identifier (e.g., "cinema", "television") |
| params.version | string | Version of the schema being used |
| id | string | Unique identifier for the response |

## Category-Specific Schemas

Each category has its own specific schema structure within the params object:

### Cinema

```json
{
  "params": {
    "category": "cinema",
    "version": "1.0",
    "formats": [
      {
        "id": "format-id",
        "name": "Format Name",
        "aspect_ratio": {
          "ratio": "w:h",
          "decimal": 1.85
        },
        "resolution": {
          "width": 1998,
          "height": 1080
        }
        // Additional properties...
      }
    ]
  }
}
```

### Mobile Phones

```json
{
  "params": {
    "category": "mobile.phones",
    "version": "1.0",
    "eras": [
      {
        "era_id": "era-id",
        "era_name": "Era Name",
        "devices": [
          {
            "id": "device-id",
            "brand": "Brand",
            "model": "Model"
            // Additional properties...
          }
        ]
      }
    ]
  }
}
```

### Television

```json
{
  "params": {
    "category": "television",
    "version": "1.0",
    "standards": [
      {
        "standard_id": "standard-id",
        "name": "Standard Name",
        "formats": [
          {
            "id": "format-id",
            "name": "Format Name"
            // Additional properties...
          }
        ]
      }
    ]
  }
}
```

### Aspect Ratios

```json
{
  "params": {
    "category": "standards.aspect_ratios",
    "version": "1.0",
    "categories": [
      {
        "category_id": "category-id",
        "category_name": "Category Name",
        "ratios": [
          {
            "id": "ratio-id",
            "name": "Ratio Name",
            "ratio": "w:h"
            // Additional properties...
          }
        ]
      }
    ]
  }
}
```

## Using the Schema

These schemas should be followed when creating new files or updating existing ones. The template processing system will automatically generate compliant JSON files from the template text files.
