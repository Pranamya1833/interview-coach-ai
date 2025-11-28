"""
Interview Coach Agent - Intelligent Rule-Based Evaluation System
Works completely offline, no API keys, no costs, no limits!
"""
import json
from agent.coach_agent_fallback import evaluate_answer_fallback

def evaluate_answer(job, question, answer):
    """
    Evaluate interview answer using intelligent rule-based system.
    Works completely offline - no API keys, no costs, no limits!
    
    This system analyzes answers based on:
    - Answer length and structure (communication)
    - Technical keywords and depth (technical knowledge)
    - Problem-solving indicators (problem-solving skills)
    - Collaboration keywords (culture fit)
    """
    return evaluate_answer_fallback(job, question, answer)
