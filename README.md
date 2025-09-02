# Test-Repo-AutoGen-Orchestor

A Multi-Agent AI Framework for Axis Max Life Insurance using AutoGen

## Overview

This project demonstrates a Proof of Concept (POC) for a multi-agent AI system that can intelligently route insurance-related queries to specialized agents:

- **Offer Agent**: Handles queries about pricing, discounts, offers, and premium rates  
- **Benefit Agent**: Handles queries about benefits, features, coverage, and plan details

## Features

🤖 **Intelligent Query Routing**: Automatically determines which agent should handle each query

📋 **PDF Content Processing**: Extracts and processes information from the Axis Max Life Smart Term Plan Plus policy document

💬 **Interactive Conversation**: Supports follow-up questions and context-aware responses

🎯 **Specialized Agents**: Each agent has domain expertise in specific areas

## Project Structure

```
Test-Repo-AutoGen-Orchestor/
├── data/
│   └── Axis-Max-STPP.pdf          # Policy document for agent knowledge base
├── orchestrator.py                 # Main application with multi-agent system
├── pyproject.toml                  # Project dependencies and configuration
├── uv.lock                        # Dependency lock file
├── .python-version                 # Python version specification
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

## Installation

### Prerequisites

- Python 3.9+
- UV package manager (recommended) or pip
- OpenAI API key

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Test-Repo-AutoGen-Orchestor
   ```

2. **Install dependencies using UV:**
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   export OPENAI_API_KEY="your-openai-api-key-here"
   ```

4. **Ensure the PDF file is in the data folder:**
   ```bash
   ls data/Axis-Max-STPP.pdf
   ```

## Usage  

### Running the Application

```bash
python orchestrator.py
```

### Example Interactions

**Query about Benefits:**
```
👤 You: Tell me all beneficiary benefits of axis max life smart plus
🤖 Assistant: The Axis Max Life Smart Term Plan Plus offers comprehensive beneficiary benefits including...
```

**Query about Offers:**
```
👤 You: Tell me all the offers and discounts available
🤖 Assistant: Here are the available offers and discounts: 1. Female Life Discount (15% flat discount)...
```

### Sample Use Cases

1. **Benefits Queries:**
   - "What are the death benefits?"
   - "Tell me about terminal illness coverage"
   - "What riders are available?"
   - "How does the survival benefit work?"

2. **Offer Queries:**
   - "What discounts are available?"  
   - "What are the premium rates?"
   - "Are there offers for non-smokers?"
   - "Tell me about the SA Booster"

## Architecture

### Agent Roles

#### Router Agent
- Analyzes incoming queries
- Routes to appropriate specialized agent
- Handles ambiguous queries

#### Benefit Agent
Specializes in:
- Death Benefits and plan variants
- Survival and Maturity Benefits
- Terminal Illness coverage
- Riders and additional features
- Coverage details and comparisons

#### Offer Agent  
Specializes in:
- Premium rates and pricing
- Discounts and offers
- Premium payment options
- Cost comparisons
- Special value propositions

### Technical Components

- **PDFProcessor**: Extracts and processes content from policy documents
- **InsuranceOrchestrator**: Main controller for agent coordination
- **AutoGen Framework**: Handles multi-agent conversations and routing

## Configuration

### LLM Configuration
The system uses OpenAI's GPT-4 model by default. You can modify the configuration in `orchestrator.py`:

```python
config_list = [
    {
        'model': 'gpt-4',
        'api_key': os.environ.get("OPENAI_API_KEY")
    }
]
```

### Agent Customization
Each agent's behavior can be customized by modifying their `system_message` in the `setup_agents()` method.

## Development

### Adding New Agents
To add new specialized agents:

1. Create the agent in `setup_agents()`
2. Update the routing logic in `classify_query()`
3. Add relevant content extraction in `PDFProcessor`

### Testing
The application includes built-in test queries that run automatically when started.

## Dependencies

- **autogen-agentchat**: Multi-agent conversation framework
- **PyPDF2**: PDF text extraction
- **openai**: LLM integration
- **python-dotenv**: Environment variable management

## Troubleshooting

**PDF Not Found Error:**
- Ensure `Axis-Max-STPP.pdf` is in the `data/` folder
- Check file permissions

**API Key Issues:**
- Verify your OpenAI API key is set correctly
- Check API key permissions and credits

**Agent Response Issues:**
- Verify internet connection for API calls
- Check token limits in configuration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for demonstration and educational purposes.

## Support

For questions or issues, please check the troubleshooting section or create an issue in the repository.

---

**Note**: This is a POC implementation. For production use, consider adding proper error handling, logging, security measures, and scalability optimizations.