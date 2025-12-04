import re
from agents.coding_agent import CodingAgent
from agents.therapy_agent import TherapyAgent
from agents.customer_service_agent import CustomerServiceAgent
from agents.research_agent import ResearchAgent
from agents.website_agent import WebsiteAgent
from agents.personal_ai import PersonalAI

def choose_agent(text: str):
    lowered = text.lower()

    if any(k in lowered for k in ["code", "python", "bug", "fix", "function", "error"]):
        return CodingAgent()

    if any(k in lowered for k in ["stress", "sad", "feel", "anxious", "therapy"]):
        return TherapyAgent()

    if any(k in lowered for k in ["order", "refund", "customer", "support"]):
        return CustomerServiceAgent()

    if any(k in lowered for k in ["research", "analyze", "search", "paper"]):
        return ResearchAgent()

    if any(k in lowered for k in ["website", "faq", "product", "info"]):
        return WebsiteAgent()

    return PersonalAI()
