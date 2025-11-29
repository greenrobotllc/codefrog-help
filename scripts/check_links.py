#!/usr/bin/env python3

"""
Help Documentation Link Checker
Scans all Markdown files in the help/ directory and validates internal links
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

# Colors for output
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
NC = '\033[0m'  # No Color

def find_help_dir() -> Path:
    """Find the help directory relative to this script."""
    script_dir = Path(__file__).parent.resolve()
    help_docs_dir = script_dir.parent
    help_dir = help_docs_dir / "help"
    
    if not help_dir.exists():
        print(f"{RED}Error: help directory not found at {help_dir}{NC}", file=sys.stderr)
        sys.exit(1)
    
    return help_dir

def extract_links(content: str) -> List[Tuple[str, str]]:
    """Extract all markdown links from content.
    
    Returns list of (link_text, link_url) tuples.
    """
    # Pattern: [text](url) or [text](url "title")
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(pattern, content)
    return matches

def is_internal_help_link(url: str) -> bool:
    """Check if URL is an internal help documentation link."""
    return bool(re.match(r'^/help/(mas|direct)/', url))

def get_expected_file_path(help_dir: Path, url: str) -> Path:
    """Get the expected file path for an internal help link."""
    # Extract section and page path
    match = re.match(r'^/help/(mas|direct)/(.+)$', url)
    if not match:
        return None
    
    section = match.group(1)
    page_with_anchor = match.group(2)
    
    # Remove anchor if present (everything after #)
    page_path = page_with_anchor.split('#')[0]
    
    # Remove trailing slash
    page_path = page_path.rstrip('/')
    
    # Build expected file path
    expected_file = help_dir / section / f"{page_path}.md"
    return expected_file

def check_links(help_dir: Path) -> Tuple[int, int, int, int, List[str]]:
    """Check all links in help documentation.
    
    Returns: (total_links, valid_links, broken_links, external_links, broken_list)
    """
    total_links = 0
    valid_links = 0
    broken_links = 0
    external_links = 0
    broken_list = []
    
    # Find all markdown files
    md_files = list(help_dir.rglob("*.md"))
    
    for md_file in md_files:
        # Get relative path from help directory
        rel_path = md_file.relative_to(help_dir)
        
        # Read file content
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"{RED}Error reading {md_file}: {e}{NC}", file=sys.stderr)
            continue
        
        # Process each line
        for line_num, line in enumerate(lines, start=1):
            # Extract links from line
            links = extract_links(line)
            
            for link_text, link_url in links:
                total_links += 1
                
                # Remove quotes from URL if present (for titles)
                link_url = link_url.strip('"\'')
                
                # Check if it's an internal help link
                if is_internal_help_link(link_url):
                    expected_file = get_expected_file_path(help_dir, link_url)
                    
                    if expected_file and expected_file.exists():
                        valid_links += 1
                    else:
                        broken_links += 1
                        expected_path = str(expected_file) if expected_file else "unknown"
                        broken_list.append(
                            f"{rel_path}:{line_num}: [{link_text}]({link_url}) -> Expected: {expected_path}"
                        )
                elif link_url.startswith(('http://', 'https://', 'mailto:')):
                    # External link - skip validation
                    external_links += 1
                elif link_url.startswith('#'):
                    # Anchor-only link (same page) - skip validation
                    external_links += 1
                elif link_url.startswith('/'):
                    # Other absolute path - could be broken, but not a help doc link
                    external_links += 1
                else:
                    # Relative link or other - skip for now
                    external_links += 1
    
    return total_links, valid_links, broken_links, external_links, broken_list

def main():
    """Main entry point."""
    help_dir = find_help_dir()
    
    print("Checking links in help documentation...")
    print(f"Help directory: {help_dir}")
    print()
    
    total_links, valid_links, broken_links, external_links, broken_list = check_links(help_dir)
    
    # Print results
    print("=" * 40)
    print("Link Check Results")
    print("=" * 40)
    print(f"Total links found: {GREEN}{total_links}{NC}")
    print(f"Valid internal links: {GREEN}{valid_links}{NC}")
    print(f"Broken internal links: {RED}{broken_links}{NC}")
    print(f"External/other links: {YELLOW}{external_links}{NC}")
    print()
    
    # Print broken links if any
    if broken_links > 0:
        print(f"{RED}Broken Links:{NC}")
        print("=" * 40)
        for broken_link in broken_list:
            print(f"{RED}✗{NC} {broken_link}")
        print()
        print(f"{RED}Please fix the broken links above.{NC}")
        sys.exit(1)
    else:
        print(f"{GREEN}✓ All internal links are valid!{NC}")
        sys.exit(0)

if __name__ == "__main__":
    main()

