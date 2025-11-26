#!/bin/bash

# Start Jekyll server for local development at help.codefrog.local
# Make sure to add this to /etc/hosts first:
#   127.0.0.1 help.codefrog.local

cd "$(dirname "$0")"

# Check if help.codefrog.local is in /etc/hosts
if ! grep -q "help.codefrog.local" /etc/hosts 2>/dev/null; then
    echo "⚠️  WARNING: help.codefrog.local not found in /etc/hosts"
    echo ""
    echo "Please add this line to /etc/hosts:"
    echo "  127.0.0.1 help.codefrog.local"
    echo ""
    echo "You can do this by running:"
    echo "  sudo sh -c 'echo \"127.0.0.1 help.codefrog.local\" >> /etc/hosts'"
    echo ""
    read -p "Press Enter to continue anyway, or Ctrl+C to exit..."
fi

# Set up environment for local gems
export GEM_HOME="$HOME/.gem"
export PATH="$GEM_HOME/bin:$PATH"

# Start Jekyll server
echo "🚀 Starting Jekyll server..."
echo "📍 Site will be available at: http://help.codefrog.local:4000/"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

bundle exec jekyll serve \
  --host help.codefrog.local \
  --port 4000 \
  --livereload \
  --watch

