#!/usr/bin/env python3

"""
Help Documentation Anchor Link Checker
Scans all Markdown files in the help/ directory and validates anchor links
"""

import os
import re
import sys
import unicodedata
from pathlib import Path
from typing import List, Tuple, Optional, Set, Dict

# Colors for output
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
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

def find_help_docs_dir() -> Path:
    """Find the help-docs directory relative to this script."""
    script_dir = Path(__file__).parent.resolve()
    return script_dir.parent

def generate_kramdown_anchor(text: str) -> str:
    """
    Generate anchor ID using kramdown's auto_id logic with Unicode support.
    Kramdown generates IDs by:
    1. Normalizing Unicode characters (NFKC normalization)
    2. Converting to lowercase
    3. Replacing spaces with hyphens
    4. Removing special characters (keeping only Unicode letters, numbers, hyphens, underscores)
    5. Collapsing multiple consecutive hyphens
    6. Removing leading/trailing hyphens
    """
    # Normalize Unicode characters (NFKC: compatibility decomposition + canonical composition)
    # This handles accented characters, ligatures, etc.
    anchor = unicodedata.normalize('NFKC', text)
    
    # Convert to lowercase
    anchor = anchor.lower()
    
    # Filter characters: keep Unicode letters, numbers, hyphens, underscores, and spaces
    # Using isalnum() which is Unicode-aware and handles all Unicode letter/number categories
    filtered_chars = []
    for char in anchor:
        if char.isalnum() or char in ['-', '_', ' ']:
            filtered_chars.append(char)
    
    anchor = ''.join(filtered_chars)
    
    # Replace spaces with hyphens
    anchor = anchor.replace(' ', '-')
    
    # Collapse multiple consecutive hyphens
    anchor = re.sub(r'-+', '-', anchor)
    
    # Remove leading/trailing hyphens
    anchor = anchor.strip('-')
    
    return anchor

def extract_headings(content: str) -> Dict[str, str]:
    """
    Extract all headings from markdown content and generate their anchor IDs.
    Returns a dict mapping anchor_id -> heading_text.
    Handles duplicate anchors by appending -1, -2, etc. (matching kramdown behavior).
    """
    headings = {}
    anchor_counts = {}
    
    # Pattern for markdown headings: # Heading, ## Heading, etc.
    # Also handles headings with optional trailing spaces and hashes
    pattern = r'^(#{1,6})\s+(.+?)(?:\s*#+\s*)?$'
    
    for line in content.split('\n'):
        match = re.match(pattern, line)
        if match:
            heading_text = match.group(2).strip()
            anchor_id = generate_kramdown_anchor(heading_text)
            
            # Handle duplicate anchors by appending -1, -2, etc.
            if anchor_id in anchor_counts:
                anchor_counts[anchor_id] += 1
                suffixed_anchor = f"{anchor_id}-{anchor_counts[anchor_id]}"
                headings[suffixed_anchor] = heading_text
            else:
                anchor_counts[anchor_id] = 0
                headings[anchor_id] = heading_text
    
    return headings

def extract_links(content: str) -> List[Tuple[str, str]]:
    """Extract all markdown links from content.
    
    Returns list of (link_text, link_url) tuples.
    """
    # Pattern: [text](url) or [text](url "title")
    # Captures URL separately from optional title
    pattern = r'\[([^\]]+)\]\(([^\s)]+)(?:\s+["\'].*?["\'])?\)'
    matches = re.findall(pattern, content)
    return matches

def is_internal_help_link(url: str) -> bool:
    """Check if URL is an internal help documentation link."""
    # Match /help/mas/, /help/direct/, /help/windows/, and /help/common/ (with or without trailing slash)
    return bool(re.match(r'^/help/(mas|direct|windows|common)(/|$)', url))

def get_expected_file_path(help_dir: Path, url: str) -> Optional[Path]:
    """Get the expected file path for an internal help link."""
    # Extract section and page path (page path can be empty for section-root URLs)
    match = re.match(r'^/help/(mas|direct|windows|common)/?(.*)$', url)
    if not match:
        return None
    
    section = match.group(1)
    page_with_anchor = match.group(2)
    
    # Remove anchor if present (everything after #)
    page_path = page_with_anchor.split('#')[0]
    
    # Remove trailing slash
    page_path = page_path.rstrip('/')
    
    # If page_path is empty, treat it as "index"
    if not page_path:
        page_path = "index"
    
    # Build expected file path
    expected_file = help_dir / section / f"{page_path}.md"
    return expected_file

def extract_anchor_from_url(url: str) -> Optional[str]:
    """Extract anchor from URL (everything after #)."""
    if '#' in url:
        return url.split('#', 1)[1]
    return None

def check_anchors(help_dir: Path) -> Tuple[int, int, int, List[str]]:
    """
    Check all anchor links in help documentation.
    
    Returns: (total_anchor_links, valid_anchors, broken_anchors, broken_list)
    """
    total_anchor_links = 0
    valid_anchors = 0
    broken_anchors = 0
    broken_list = []
    
    # First pass: collect all headings from all markdown files
    # This allows us to check cross-file anchor links
    all_headings: Dict[Path, Dict[str, str]] = {}
    
    # Get help-docs root directory to check root index.md
    help_docs_dir = find_help_docs_dir()
    
    # Find all markdown files in help/ directory
    md_files = list(help_dir.rglob("*.md"))
    
    # Also check root index.md if it exists
    root_index = help_docs_dir / "index.md"
    if root_index.exists():
        md_files.append(root_index)
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            headings = extract_headings(content)
            all_headings[md_file] = headings
        except (OSError, UnicodeDecodeError) as e:
            print(f"{YELLOW}Warning: Could not read {md_file}: {e}{NC}", file=sys.stderr)
            continue
    
    # Second pass: check all anchor links
    for md_file in md_files:
        # Get relative path - handle both help/ subdirectory and root files
        try:
            rel_path = md_file.relative_to(help_dir)
        except ValueError:
            # File is outside help_dir (like root index.md)
            rel_path = md_file.relative_to(help_docs_dir)
        
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except (OSError, UnicodeDecodeError) as e:
            print(f"{YELLOW}Warning: Could not read {md_file}: {e}{NC}", file=sys.stderr)
            continue
        
        # Process each line
        for line_num, line in enumerate(lines, start=1):
            links = extract_links(line)
            
            for link_text, link_url in links:
                # Remove quotes from URL if present
                link_url = link_url.strip('"\'')
                
                # Skip Jekyll template syntax (Liquid templates)
                if '{{' in link_url or '{%' in link_url:
                    continue
                
                # Check if it's an anchor link (starts with # or contains #)
                anchor = None
                if link_url.startswith('#'):
                    # Same-page anchor
                    anchor = link_url[1:]
                    target_file = md_file
                elif '#' in link_url and is_internal_help_link(link_url):
                    # Cross-file anchor link
                    anchor = extract_anchor_from_url(link_url)
                    target_file = get_expected_file_path(help_dir, link_url)
                else:
                    # Not an anchor link, skip
                    continue
                
                if not anchor:
                    continue
                
                total_anchor_links += 1
                
                # Check if target file exists
                if target_file is None or not target_file.exists():
                    broken_anchors += 1
                    # Include original link URL when target_file is None for better debugging
                    target_info = link_url if target_file is None else str(target_file)
                    broken_list.append(
                        f"{rel_path}:{line_num}: [{link_text}]({link_url}) -> Target file not found: {target_info}"
                    )
                    continue
                
                # Get headings from target file
                if target_file not in all_headings:
                    # Try to read it now
                    try:
                        with open(target_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                        headings = extract_headings(content)
                        all_headings[target_file] = headings
                    except (OSError, UnicodeDecodeError) as e:
                        broken_anchors += 1
                        broken_list.append(
                            f"{rel_path}:{line_num}: [{link_text}]({link_url}) -> Could not read target file: {e}"
                        )
                        continue
                
                headings = all_headings[target_file]
                
                # Normalize anchor (kramdown generates lowercase anchors)
                normalized_anchor = anchor.lower()
                
                # Check if anchor exists
                if normalized_anchor in headings:
                    valid_anchors += 1
                else:
                    broken_anchors += 1
                    # Find similar anchors for helpful error message
                    similar = [h for h in headings.keys() if normalized_anchor in h or h in normalized_anchor]
                    similar_msg = ""
                    if similar:
                        similar_msg = f" (similar: {', '.join(similar[:3])})"
                    
                    # Get target file path for error message - handle files outside help_dir
                    try:
                        target_path = target_file.relative_to(help_dir)
                    except ValueError:
                        # File is outside help_dir (like root index.md)
                        try:
                            target_path = target_file.relative_to(help_docs_dir)
                        except ValueError:
                            # Fallback to just the filename if both fail
                            target_path = target_file.name
                    
                    broken_list.append(
                        f"{rel_path}:{line_num}: [{link_text}]({link_url}) -> Anchor '#{anchor}' not found in {target_path}{similar_msg}"
                    )
    
    return total_anchor_links, valid_anchors, broken_anchors, broken_list

def main():
    """Main entry point."""
    help_dir = find_help_dir()
    
    print("Checking anchor links in help documentation...")
    print(f"Help directory: {help_dir}")
    print()
    
    total_anchors, valid_anchors, broken_anchors, broken_list = check_anchors(help_dir)
    
    # Print results
    print("=" * 40)
    print("Anchor Link Check Results")
    print("=" * 40)
    print(f"Total anchor links found: {BLUE}{total_anchors}{NC}")
    print(f"Valid anchor links: {GREEN}{valid_anchors}{NC}")
    print(f"Broken anchor links: {RED}{broken_anchors}{NC}")
    print()
    
    # Print broken anchors if any
    if broken_anchors > 0:
        print(f"{RED}Broken Anchor Links:{NC}")
        print("=" * 40)
        for broken_link in broken_list:
            print(f"{RED}✗{NC} {broken_link}")
        print()
        print(f"{RED}Please fix the broken anchor links above.{NC}")
        print()
        print(f"{YELLOW}Tip: Anchor IDs are generated from headings using kramdown's auto_id logic:{NC}")
        print(f"  - Convert to lowercase")
        print(f"  - Replace spaces with hyphens")
        print(f"  - Remove special characters")
        print(f"  - Collapse multiple hyphens")
        sys.exit(1)
    else:
        print(f"{GREEN}✓ All anchor links are valid!{NC}")
        sys.exit(0)

if __name__ == "__main__":
    main()

