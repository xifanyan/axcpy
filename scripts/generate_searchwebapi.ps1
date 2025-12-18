# Generate SearchWebAPI client using Microsoft Kiota

<#
.SYNOPSIS
    Generates the Python client from OpenAPI specification using Kiota

.DESCRIPTION
    This script generates the SearchWebAPI Python client code using Microsoft Kiota.
    
.PREREQUISITES
    - Kiota CLI installed (npm install -g @microsoft/kiota or dotnet tool install -g Microsoft.OpenApi.Kiota)
    - OpenAPI specification file (openapi.yaml or openapi.json)

.EXAMPLE
    .\generate_searchwebapi.ps1
#>

$ErrorActionPreference = "Stop"

Write-Host "Generating SearchWebAPI client with Kiota..." -ForegroundColor Cyan

# Configuration
$OPENAPI_SPEC = "openapi.yaml"  # Update with actual path
$OUTPUT_DIR = "src/axcpy/searchwebapi/generated"
$CLASS_NAME = "SearchWebAPIClient"
$NAMESPACE = "axcpy.searchwebapi.generated"

# Check if OpenAPI spec exists
if (-not (Test-Path $OPENAPI_SPEC)) {
    Write-Host "Error: OpenAPI specification not found at $OPENAPI_SPEC" -ForegroundColor Red
    Write-Host "Please provide the OpenAPI specification file" -ForegroundColor Yellow
    exit 1
}

# Check if Kiota is installed
$kiotaExists = Get-Command kiota -ErrorAction SilentlyContinue
if (-not $kiotaExists) {
    Write-Host "Error: Kiota CLI not found" -ForegroundColor Red
    Write-Host "Install with: npm install -g @microsoft/kiota" -ForegroundColor Yellow
    Write-Host "Or: dotnet tool install -g Microsoft.OpenApi.Kiota" -ForegroundColor Yellow
    exit 1
}

# Generate client
Write-Host "Running Kiota generation..." -ForegroundColor Green

kiota generate `
    --language python `
    --openapi $OPENAPI_SPEC `
    --output $OUTPUT_DIR `
    --class-name $CLASS_NAME `
    --namespace-name $NAMESPACE `
    --clear-output

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Client generation complete!" -ForegroundColor Green
    Write-Host "Generated files in: $OUTPUT_DIR" -ForegroundColor Cyan
} else {
    Write-Host "✗ Client generation failed!" -ForegroundColor Red
    exit $LASTEXITCODE
}
