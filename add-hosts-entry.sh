#!/bin/bash

# Add help.codefrog.local to /etc/hosts

if grep -q "help.codefrog.local" /etc/hosts 2>/dev/null; then
    echo "✅ help.codefrog.local already exists in /etc/hosts"
    exit 0
fi

echo "Adding help.codefrog.local to /etc/hosts..."
echo "You will be prompted for your password."

sudo sh -c 'echo "127.0.0.1 help.codefrog.local" >> /etc/hosts'

if [ $? -eq 0 ]; then
    echo "✅ Successfully added help.codefrog.local to /etc/hosts"
    echo ""
    echo "You can now start the Jekyll server with:"
    echo "  ./start-local.sh"
else
    echo "❌ Failed to add entry. Please run manually:"
    echo "  sudo sh -c 'echo \"127.0.0.1 help.codefrog.local\" >> /etc/hosts'"
    exit 1
fi

