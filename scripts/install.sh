#!/bin/bash

# ChatKali Skill Installer
# Installs ChatKali to OpenAI Codex and Claude Code skill directories.

REPO_URL="https://github.com/tzf1003/ChatKali.git"
INSTALL_DIR_CODEX="$HOME/.codex/skills/chatkali"
INSTALL_DIR_CLAUDE="$HOME/.claude/skills/chatkali"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Installing ChatKali Skills...${NC}"

# Function to install/update repo
install_repo() {
    local target_dir=$1
    local name=$2

    if [ -d "$target_dir" ]; then
        echo -e "${BLUE}🔄 Updating $name in $target_dir...${NC}"
        if git -C "$target_dir" pull; then
            echo -e "${GREEN}✓ Successfully updated $name${NC}"
        else
            echo "⚠️  Failed to update $name. Please check git status in $target_dir"
        fi
    else
        echo -e "${BLUE}⬇️  Cloning $name to $target_dir...${NC}"
        mkdir -p "$(dirname "$target_dir")"
        if git clone "$REPO_URL" "$target_dir"; then
            echo -e "${GREEN}✓ Successfully installed $name${NC}"
        else
            echo "❌ Failed to clone $name"
        fi
    fi
}

# 1. OpenAI Codex
install_repo "$INSTALL_DIR_CODEX" "OpenAI Codex"

# 2. Claude Code
install_repo "$INSTALL_DIR_CLAUDE" "Claude Code"

echo ""
echo -e "${GREEN}✅ Installation Complete!${NC}"
echo "Please restart your agent (Codex/Claude) to load the new skills."
echo "  - Codex: Type '/skills' to verify."
echo "  - Claude: Ask 'List all available Skills' to verify."
