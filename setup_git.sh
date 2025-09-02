#!/bin/bash

# Git Repository Setup Script for Test-Repo-AutoGen-Orchestor
# Multi-Agent AI Framework for Axis Max Life Insurance

echo "🚀 Setting up Test-Repo-AutoGen-Orchestor Git Repository"
echo "========================================================"

# Initialize Git repository
echo "📁 Initializing Git repository..."
git init
echo "✅ Git repository initialized"

# Add all files to Git
echo "📝 Adding files to Git..."
git add .
echo "✅ Files added to staging"

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Multi-Agent AI Framework for Axis Max Life Insurance

Features:
- AutoGen-based multi-agent system
- Offer Agent for pricing/discounts queries  
- Benefit Agent for coverage/features queries
- PDF content processing from policy document
- Intelligent query routing
- Interactive conversation support
- Complete project setup with dependencies

Files included:
- orchestrator.py (Main application)
- data/Axis-Max-STPP.pdf (Policy document)  
- README.md (Documentation)
- pyproject.toml (Dependencies)
- uv.lock (Lock file)
- .python-version (Python 3.11.0)
- .gitignore (Git ignore rules)
- test_system.py (Test script)"

echo "✅ Initial commit created"

# Show repository status
echo "📊 Repository status:"
git log --oneline
echo ""
git status

echo ""
echo "🎉 Git repository setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Set up remote repository (GitHub/GitLab)"
echo "2. git remote add origin <remote-url>"  
echo "3. git push -u origin main"
echo ""
echo "🛠️ To run the application:"
echo "1. Install dependencies: uv sync"
echo "2. Set API key: export OPENAI_API_KEY='your-key'"
echo "3. Run: python orchestrator.py"