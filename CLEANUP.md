# Media Grids - Cleanup Instructions

## Deprecated Folders

The following folders have been marked as deprecated after reorganizing the project structure:

- `./cinema_deprecated/` → Moved to `./domains/display/cinema/`
- `./mobile_deprecated/` → Moved to `./domains/display/mobile/`
- `./television_deprecated/` → Moved to `./domains/display/television/`
- `./print_deprecated/` → Moved to `./domains/content/print/`
- `./wearables_deprecated/` → Moved to `./domains/display/wearable/`
- `./scripts_deprecated/` → Moved to `./tools/generators/`
- `./standards/color-spaces_deprecated/` → Moved to `./standards/color/spaces/`

## Cleanup Procedure

To finalize the cleanup process:

1. Verify that all content from deprecated folders has been properly transferred to the new structure
2. Check that no untracked or unique files remain in the deprecated folders 
3. Run the following commands to permanently remove deprecated folders:

```bash
# Remove deprecated top-level folders
rm -rf ./cinema_deprecated
rm -rf ./mobile_deprecated
rm -rf ./television_deprecated
rm -rf ./print_deprecated
rm -rf ./wearables_deprecated
rm -rf ./scripts_deprecated

# Remove deprecated standards subfolder
rm -rf ./standards/color-spaces_deprecated
```

## Verification Before Deletion

Before removing deprecated folders, consider running a diff tool to ensure nothing important will be lost:

```bash
# Example diff command for cinema files
diff -r ./cinema_deprecated ./domains/display/cinema

# Example diff command for color spaces
diff -r ./standards/color-spaces_deprecated ./standards/color/spaces
```

## Post-Cleanup Verification

After removing the deprecated folders, validate the project structure to ensure it contains all required components:

```bash
# Check the main domain structure
find ./domains -type f | sort

# Check the standards structure
find ./standards -type f | sort
```

## Cleanup Completion

Once the deprecated folders have been removed and the structure verified, you can also remove this cleanup instructions file.
