#!/bin/bash

# Help Documentation Link Checker
# Scans all Markdown files in the help/ directory and validates internal links

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HELP_DOCS_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
HELP_DIR="$HELP_DOCS_DIR/help"

# Check if help directory exists
if [ ! -d "$HELP_DIR" ]; then
    echo -e "${RED}Error: help directory not found at $HELP_DIR${NC}" >&2
    exit 1
fi

# Temporary files
TEMP_BROKEN=$(mktemp)
TEMP_COUNTS=$(mktemp)
trap "rm -f $TEMP_BROKEN $TEMP_COUNTS" EXIT

# Initialize counters in temp file
echo "0 0 0 0" > "$TEMP_COUNTS"  # total valid broken external

echo "Checking links in help documentation..."
echo "Help directory: $HELP_DIR"
echo ""

# Find all markdown files in help directory
find "$HELP_DIR" -name "*.md" -type f | while IFS= read -r file; do
    # Get relative path from help directory
    rel_path="${file#$HELP_DIR/}"
    
    # Read file line by line
    line_num=0
    while IFS= read -r line || [ -n "$line" ]; do
        ((line_num++))
        
        # Extract all markdown links from the line using grep
        # Pattern: [text](url)
        # Capture output first to avoid grep exit code 1 aborting the script
        link_matches=$(echo "$line" | grep -oE '\[([^\]]+)\]\(([^)]+)\)' || true)
        if [ -n "$link_matches" ]; then
            echo "$link_matches" | while IFS= read -r link_match; do
            # Extract link text and URL
            link_text=$(echo "$link_match" | sed -E 's/\[([^\]]+)\]\([^)]+\)/\1/')
            link_url=$(echo "$link_match" | sed -E 's/\[[^\]]+\]\(([^)]+)\)/\1/')
            
            # Remove quotes from URL if present (for titles)
            link_url=$(echo "$link_url" | sed -E "s/^['\"](.*)['\"]$/\1/")
            
            # Read current counts
            read total valid broken external < "$TEMP_COUNTS"
            ((total++))
            
            # Check if it's an internal help link
            # Pattern matches both /help/mas/ and /help/mas (with or without trailing slash)
            if echo "$link_url" | grep -qE '^/help/(mas|direct)(/|$)'; then
                # Extract section (mas or direct)
                if echo "$link_url" | grep -qE '^/help/mas'; then
                    section="mas"
                    # Remove /help/mas/ or /help/mas prefix, handling both cases
                    page_with_anchor=$(echo "$link_url" | sed -E 's|^/help/mas/?||')
                else
                    section="direct"
                    # Remove /help/direct/ or /help/direct prefix, handling both cases
                    page_with_anchor=$(echo "$link_url" | sed -E 's|^/help/direct/?||')
                fi
                
                # Remove anchor if present (everything after #)
                page_path=$(echo "$page_with_anchor" | sed 's/#.*//')
                
                # Remove trailing slash
                page_path="${page_path%/}"
                
                # If page_path is empty, treat it as "index"
                if [ -z "$page_path" ]; then
                    page_path="index"
                fi
                
                # Check if file exists
                expected_file="$HELP_DIR/$section/$page_path.md"
                
                if [ -f "$expected_file" ]; then
                    ((valid++))
                else
                    ((broken++))
                    echo "$rel_path:$line_num: [$link_text]($link_url) -> Expected: $expected_file" >> "$TEMP_BROKEN"
                fi
            elif echo "$link_url" | grep -qE '^https?://'; then
                # External HTTP/HTTPS link - skip validation
                ((external++))
            elif echo "$link_url" | grep -qE '^mailto:'; then
                # Email link - skip validation
                ((external++))
            elif echo "$link_url" | grep -qE '^#'; then
                # Anchor-only link (same page) - skip validation
                ((external++))
            elif echo "$link_url" | grep -qE '^/'; then
                # Other absolute path - could be broken, but not a help doc link
                ((external++))
            else
                # Relative link or other - skip for now
                ((external++))
            fi
            
            # Write updated counts back
            echo "$total $valid $broken $external" > "$TEMP_COUNTS"
            done
        fi
    done < "$file"
done

# Read final counts
read total_links valid_links broken_links external_links < "$TEMP_COUNTS"

# Print results
echo "========================================="
echo "Link Check Results"
echo "========================================="
echo -e "Total links found: ${GREEN}$total_links${NC}"
echo -e "Valid internal links: ${GREEN}$valid_links${NC}"
echo -e "Broken internal links: ${RED}$broken_links${NC}"
echo -e "External/other links: ${YELLOW}$external_links${NC}"
echo ""

# Print broken links if any
if [ $broken_links -gt 0 ]; then
    echo -e "${RED}Broken Links:${NC}"
    echo "========================================="
    while IFS= read -r broken_link; do
        echo -e "${RED}✗${NC} $broken_link"
    done < "$TEMP_BROKEN"
    echo ""
    echo -e "${RED}Please fix the broken links above.${NC}"
    exit 1
else
    echo -e "${GREEN}✓ All internal links are valid!${NC}"
    exit 0
fi
