"""
Multi-Agent AI Framework for Axis Max Life Insurance
Using AutoGen for Offer Agent and Benefit Agent orchestration
"""

import os
import autogen
import PyPDF2
from typing import Dict, List
import re
from pathlib import Path

# Configuration for the LLM
config_list = [
    {
        'model': 'gpt-4',
        'api_key': os.environ.get("OPENAI_API_KEY", "your-api-key-here")
    }
]

llm_config = {"config_list": config_list, "timeout": 600}

class PDFProcessor:
    """Handle PDF content extraction and processing"""

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.content = self._extract_text()

    def _extract_text(self) -> str:
        """Extract text from PDF file"""
        try:
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                return text
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return "PDF content not available"

    def get_benefits_content(self) -> str:
        """Extract benefits-related content"""
        benefits_keywords = [
            "death benefit", "survival benefit", "maturity benefit",
            "terminal illness", "cover continuance", "insta payment",
            "lifeline plus", "riders", "plan variants", "features"
        ]

        lines = self.content.split('\n')
        relevant_lines = []

        for line in lines:
            if any(keyword.lower() in line.lower() for keyword in benefits_keywords):
                relevant_lines.extend([line] + lines[max(0, lines.index(line)-2):lines.index(line)+3])

        return '\n'.join(set(relevant_lines))

    def get_offers_content(self) -> str:
        """Extract offers and discounts related content"""
        offers_keywords = [
            "discount", "premium", "offer", "rates", "pricing",
            "first year discount", "female life discount", "sa booster",
            "non-smoker", "employee discount", "special exit value"
        ]

        lines = self.content.split('\n')
        relevant_lines = []

        for line in lines:
            if any(keyword.lower() in line.lower() for keyword in offers_keywords):
                relevant_lines.extend([line] + lines[max(0, lines.index(line)-2):lines.index(line)+3])

        return '\n'.join(set(relevant_lines))

class InsuranceOrchestrator:
    """Main orchestrator for the multi-agent system"""

    def __init__(self):
        self.pdf_processor = PDFProcessor("data/Axis-Max-STPP.pdf")
        self.setup_agents()

    def setup_agents(self):
        """Initialize the AutoGen agents"""

        # User Proxy Agent
        self.user_proxy = autogen.UserProxyAgent(
            name="user_proxy",
            human_input_mode="NEVER",
            max_consecutive_auto_reply=10,
            is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
            code_execution_config={"work_dir": "working_dir", "use_docker": False},
        )

        # Router Agent - determines which specialized agent to use
        self.router_agent = autogen.AssistantAgent(
            name="router_agent",
            llm_config=llm_config,
            system_message="""You are a router agent for Axis Max Life Insurance queries. 
            Analyze the user's question and determine if it's about:
            1. OFFERS/DISCOUNTS/PRICING - route to Offer_Agent
            2. BENEFITS/FEATURES/COVERAGE - route to Benefit_Agent

            Respond with only: "ROUTE_TO: [Agent_Name]" and briefly explain why.
            Examples:
            - "tell me about discounts" → "ROUTE_TO: Offer_Agent - User asking about discounts/pricing"
            - "what are the death benefits" → "ROUTE_TO: Benefit_Agent - User asking about coverage benefits"
            """
        )

        # Benefit Agent - handles benefits, features, coverage questions
        self.benefit_agent = autogen.AssistantAgent(
            name="Benefit_Agent",
            llm_config=llm_config,
            system_message=f"""You are the Benefit Agent for Axis Max Life Smart Term Plan Plus.
            Your role is to answer questions about benefits, features, coverage, and plan details.

            Use this information from the policy document:
            {self.pdf_processor.get_benefits_content()[:4000]}

            Key areas you handle:
            - Death Benefits and plan variants
            - Survival and Maturity Benefits  
            - Terminal Illness coverage
            - Riders and additional features
            - Cover Continuance Benefit
            - Insta Payment features
            - Plan comparison and features

            Always provide accurate, detailed responses based on the policy document.
            If asked about pricing/discounts, redirect to the Offer Agent.
            """
        )

        # Offer Agent - handles pricing, discounts, offers
        self.offer_agent = autogen.AssistantAgent(
            name="Offer_Agent", 
            llm_config=llm_config,
            system_message=f"""You are the Offer Agent for Axis Max Life Smart Term Plan Plus.
            Your role is to answer questions about pricing, discounts, offers, and premium rates.

            Use this information from the policy document:
            {self.pdf_processor.get_offers_content()[:4000]}

            Key areas you handle:
            - Premium rates and pricing
            - Discounts (Employee, First Year, Female Life, Non-Smoker)
            - SA Booster options
            - Special Exit Value benefits
            - Premium payment terms and modes
            - Cost comparisons between variants

            Always provide accurate pricing information based on the policy document.
            If asked about benefits/coverage details, redirect to the Benefit Agent.
            """
        )

    def classify_query(self, query: str) -> str:
        """Determine which agent should handle the query"""
        offer_keywords = [
            "discount", "price", "premium", "cost", "offer", "rate", 
            "cheap", "expensive", "payment", "save", "money", "fee"
        ]

        benefit_keywords = [
            "benefit", "coverage", "death", "survival", "maturity", 
            "terminal", "rider", "feature", "protection", "claim", "payout"
        ]

        query_lower = query.lower()
        offer_score = sum(1 for keyword in offer_keywords if keyword in query_lower)
        benefit_score = sum(1 for keyword in benefit_keywords if keyword in query_lower)

        if offer_score > benefit_score:
            return "Offer_Agent"
        elif benefit_score > offer_score:
            return "Benefit_Agent"
        else:
            # Use router agent for ambiguous cases
            return "Router_Agent"

    def process_query(self, query: str) -> str:
        """Process user query and return appropriate agent response"""

        # Classify the query
        selected_agent = self.classify_query(query)

        print(f"🤖 Query routed to: {selected_agent}")

        if selected_agent == "Offer_Agent":
            agent = self.offer_agent
        elif selected_agent == "Benefit_Agent":
            agent = self.benefit_agent
        else:
            # Use router agent first, then the appropriate specialist
            router_response = self.router_agent.generate_reply(
                messages=[{"content": query, "role": "user"}]
            )
            print(f"Router decision: {router_response}")

            if "Offer_Agent" in router_response:
                agent = self.offer_agent
            else:
                agent = self.benefit_agent

        # Get response from selected agent
        response = agent.generate_reply(
            messages=[{"content": query, "role": "user"}]
        )

        return response

    def start_conversation(self):
        """Start interactive conversation loop"""
        print("🏢 Axis Max Life Smart Term Plan Plus - AI Assistant")
        print("Ask me about benefits, features, offers, or pricing!")
        print("Type 'exit' to quit\n")

        conversation_history = []

        while True:
            try:
                user_input = input("\n👤 You: ").strip()

                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("👋 Thank you for using Axis Max Life Assistant!")
                    break

                if not user_input:
                    continue

                print(f"\n🤖 Processing your query...")
                response = self.process_query(user_input)
                print(f"\n💬 Assistant: {response}")

                # Store conversation for context
                conversation_history.append({
                    "user": user_input,
                    "assistant": response
                })

            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                print("Please try again with a different question.")

def main():
    """Main function to run the orchestrator"""
    try:
        orchestrator = InsuranceOrchestrator()

        # Test examples
        print("🧪 Testing the system with sample queries:\n")

        test_queries = [
            "Tell me all beneficiary benefits of axis max life smart plus",
            "Tell me all the offers and discounts available",
            "What is the death benefit coverage?",
            "Are there any discounts for female customers?"
        ]

        for query in test_queries:
            print(f"👤 Test Query: {query}")
            response = orchestrator.process_query(query)
            print(f"🤖 Response: {response[:200]}...\n")
            print("-" * 50)

        # Start interactive mode
        orchestrator.start_conversation()

    except Exception as e:
        print(f"❌ Error initializing system: {e}")
        print("Please check if the PDF file exists in the data/ folder")

if __name__ == "__main__":
    main()