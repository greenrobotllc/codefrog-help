#!/usr/bin/env bash
set -euo pipefail

# Deploy Jekyll help documentation to GitHub Pages
# This script builds the Jekyll site and deploys it to the gh-pages branch

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(git rev-parse --show-toplevel)"
DOCS_DIR="${REPO_ROOT}/landing-page/public_html"
GIT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if we're on main branch
if [ "$GIT_BRANCH" != "main" ] && [ "$GIT_BRANCH" != "master" ]; then
    echo -e "${YELLOW}Warning: Not on main/master branch. Current branch: $GIT_BRANCH${NC}"
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
    echo -e "${RED}Error: You have uncommitted changes. Please commit or stash them before deploying.${NC}"
    exit 1
fi

# Check if docs directory exists
if [ ! -d "$DOCS_DIR" ]; then
    echo -e "${RED}Error: Documentation directory not found: $DOCS_DIR${NC}"
    exit 1
fi

cd "$DOCS_DIR"

# Check if bundle is available
if ! command -v bundle &> /dev/null; then
    echo -e "${RED}Error: bundle command not found. Please install Ruby and Bundler.${NC}"
    echo "Install with: gem install bundler"
    exit 1
fi

echo -e "${GREEN}Installing dependencies...${NC}"
bundle install

echo -e "${GREEN}Building Jekyll site...${NC}"
JEKYLL_ENV=production bundle exec jekyll build -d _site

# Check if build was successful
if [ ! -d "_site" ]; then
    echo -e "${RED}Error: Jekyll build failed. _site directory not found.${NC}"
    exit 1
fi

# Check if CNAME exists in _site
if [ ! -f "_site/CNAME" ]; then
    echo -e "${YELLOW}Warning: CNAME file not found in _site. Copying from source...${NC}"
    if [ -f "CNAME" ]; then
        cp CNAME _site/CNAME
    else
        echo -e "${RED}Error: CNAME file not found in source either.${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}Deploying to gh-pages branch...${NC}"

# Create or update gh-pages branch using worktree
GIT_WORKTREE_DIR="${REPO_ROOT}/.git-worktree-gh-pages"

# Clean up old worktree if it exists
if [ -d "$GIT_WORKTREE_DIR" ]; then
    echo "Removing old worktree..."
    git worktree remove "$GIT_WORKTREE_DIR" 2>/dev/null || rm -rf "$GIT_WORKTREE_DIR"
fi

# Create worktree for gh-pages
git worktree add -B gh-pages "$GIT_WORKTREE_DIR" origin/gh-pages 2>/dev/null || \
    git worktree add -B gh-pages "$GIT_WORKTREE_DIR" HEAD

# Copy built site to worktree
echo "Copying built site to gh-pages branch..."
rsync -av --delete --exclude='.git' _site/ "$GIT_WORKTREE_DIR/"

cd "$GIT_WORKTREE_DIR"

# Commit and push
git add -A
if git diff-index --quiet HEAD --; then
    echo -e "${YELLOW}No changes to deploy.${NC}"
else
    git commit -m "Deploy help documentation $(date +'%Y-%m-%d %H:%M:%S')"
    echo -e "${GREEN}Pushing to gh-pages branch...${NC}"
    git push origin gh-pages
    echo -e "${GREEN}Deployment complete!${NC}"
    echo -e "${GREEN}Site should be available at: https://help.codefrog.app${NC}"
fi

# Clean up worktree
cd "$REPO_ROOT"
git worktree remove "$GIT_WORKTREE_DIR"

echo -e "${GREEN}Done!${NC}"

