#!/bin/bash
# Generate SearchWebAPI client using Microsoft Kiota

# This script generates the Python client from OpenAPI specification
# Prerequisites:
#   - Kiota CLI installed
#   - OpenAPI specification file (openapi.yaml or openapi.json)

set -e

echo "Generating SearchWebAPI client with Kiota..."

# Configuration
OPENAPI_SPEC="openapi.yaml"  # Update with actual path
OUTPUT_DIR="src/axcpy/searchwebapi/generated"
CLASS_NAME="SearchWebAPIClient"
NAMESPACE="axcpy.searchwebapi.generated"

# Check if OpenAPI spec exists
if [ ! -f "$OPENAPI_SPEC" ]; then
    echo "Error: OpenAPI specification not found at $OPENAPI_SPEC"
    echo "Please provide the OpenAPI specification file"
    exit 1
fi

# Generate client
kiota generate \
    --language python \
    --openapi "$OPENAPI_SPEC" \
    --output "$OUTPUT_DIR" \
    --class-name "$CLASS_NAME" \
    --namespace-name "$NAMESPACE" \
    --clear-output

echo "✓ Client generation complete!"
echo "Generated files in: $OUTPUT_DIR"
