# Quick Start Guide - Test-Repo-AutoGen-Orchestor

## 🚀 Fast Setup (5 minutes)

### Step 1: Extract and Setup
```bash
# Extract the ZIP file
unzip Test-Repo-AutoGen-Orchestor.zip
cd Test-Repo-AutoGen-Orchestor

# Make setup script executable and run it
chmod +x setup_git.sh
./setup_git.sh
```

### Step 2: Install Dependencies

**Option A: Using UV (Recommended)**
```bash
# Install UV if you don't have it
pip install uv

# Install dependencies
uv sync
```

**Option B: Using Pip**
```bash
pip install -r requirements.txt
```

### Step 3: Set Environment
```bash
# Set your OpenAI API key
export OPENAI_API_KEY="your-openai-api-key-here"

# Verify PDF file exists
ls data/Axis-Max-STPP.pdf
```

### Step 4: Run and Test
```bash
# Test the system first
python test_system.py

# Run the main application
python orchestrator.py
```

## 🎯 Sample Queries to Try

**Benefits Queries (→ Benefit Agent):**
- "Tell me all beneficiary benefits of axis max life smart plus"
- "What are the death benefits and coverage options?"
- "How does terminal illness coverage work?"
- "Tell me about the plan variants available"
- "What riders can I add to my policy?"

**Offers Queries (→ Offer Agent):**
- "Tell me all the offers and discounts available"  
- "What discounts do you have for female customers?"
- "Are there any premium savings for non-smokers?"
- "What is the SA Booster option?"
- "Tell me about limited pay premium savings"

## 🏗️ Architecture Overview

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   User Query    │───▶│  Router Agent    │───▶│ Specialized     │
│                 │    │                  │    │ Agent Response  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
              ┌─────────────┐    ┌─────────────┐
              │Benefit Agent│    │Offer Agent  │
              │             │    │             │
              │• Death Benefits  │• Discounts  │
              │• Coverage   │    │• Pricing    │
              │• Riders     │    │• Offers     │
              │• Features   │    │• Premiums   │
              └─────────────┘    └─────────────┘
```

## 📁 Repository Structure

```
Test-Repo-AutoGen-Orchestor/
├── 📄 orchestrator.py          # Main multi-agent application
├── 📁 data/
│   └── 📄 Axis-Max-STPP.pdf   # Insurance policy document (1.45MB)
├── 📄 README.md                # Complete documentation
├── 📄 pyproject.toml           # Project configuration (UV)
├── 📄 requirements.txt         # Dependencies (Pip)
├── 📄 uv.lock                  # Dependency lock file
├── 📄 .python-version          # Python 3.11.0
├── 📄 .gitignore              # Git ignore rules
├── 📄 test_system.py          # Test and demo script
├── 📄 setup_git.sh            # Git setup automation
└── 📄 QUICKSTART.md           # This guide
```

## ⚡ Key Features

✅ **Intelligent Query Routing**: Automatically routes questions to the right agent  
✅ **PDF Content Processing**: Extracts policy information for agent knowledge  
✅ **Context-Aware Conversations**: Maintains history for follow-up questions  
✅ **Specialized Agents**: Domain expertise in benefits vs offers  
✅ **Interactive Mode**: Console-based conversation interface  
✅ **Error Handling**: Graceful fallbacks and error recovery  

## 🔧 Troubleshooting

**Common Issues:**

1. **PDF Not Found**: Ensure `data/Axis-Max-STPP.pdf` exists and is readable
2. **API Key Error**: Set `OPENAI_API_KEY` environment variable correctly
3. **Import Errors**: Install dependencies with `uv sync` or `pip install -r requirements.txt`
4. **Permission Denied**: Run `chmod +x setup_git.sh` before executing

**Test Everything:**
```bash
python test_system.py  # Runs system tests without API calls
```

## 🎉 Success Indicators

When working correctly, you should see:
- ✅ Query routing to correct agents (Benefits vs Offers)
- ✅ Detailed responses based on PDF content
- ✅ Interactive conversation mode
- ✅ Context-aware follow-up handling

## 📞 Next Steps

1. **Customize Agents**: Modify system messages in `orchestrator.py`
2. **Add More Agents**: Extend for Claims, Underwriting, etc.
3. **Web Interface**: Build a web UI for better UX
4. **Production Deploy**: Add logging, monitoring, security

---

**Ready to start?** Run `python orchestrator.py` and ask about Axis Max Life benefits or offers!
