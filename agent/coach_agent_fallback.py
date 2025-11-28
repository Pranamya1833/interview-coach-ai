"""
Intelligent Interview Evaluation System
Works completely offline - no API keys, no costs, no limits!
"""
import json
import re

def evaluate_answer_fallback(job, question, answer):
    """
    Intelligent rule-based evaluation system.
    Analyzes answers using keyword detection, structure analysis, and scoring algorithms.
    Provides meaningful, actionable feedback without requiring any external APIs.
    """
    # Basic scoring based on answer characteristics
    answer_lower = answer.lower()
    answer_length = len(answer.split())
    
    # Communication score (based on length and structure)
    comm_score = min(5, max(1, answer_length // 30 + 2))
    
    # Technical depth (based on technical keywords)
    tech_keywords = ['api', 'database', 'algorithm', 'system', 'architecture', 'framework', 
                     'code', 'implementation', 'optimization', 'scalability', 'performance',
                     'security', 'testing', 'deployment', 'integration', 'design', 'pattern']
    tech_count = sum(1 for keyword in tech_keywords if keyword in answer_lower)
    tech_score = min(5, max(1, tech_count // 2 + 2))
    
    # Problem solving (based on problem-solving indicators)
    problem_keywords = ['challenge', 'problem', 'solution', 'issue', 'resolved', 'fixed',
                       'improved', 'optimized', 'solved', 'addressed', 'overcame']
    problem_count = sum(1 for keyword in problem_keywords if keyword in answer_lower)
    problem_score = min(5, max(1, problem_count // 2 + 2))
    
    # Culture fit (based on collaboration and teamwork indicators)
    culture_keywords = ['team', 'collaborate', 'work together', 'helped', 'supported',
                       'communicated', 'discussed', 'feedback', 'learned', 'mentored']
    culture_count = sum(1 for keyword in culture_keywords if keyword in answer_lower)
    culture_score = min(5, max(1, culture_count // 2 + 2))
    
    # Generate explanations
    explanations = {
        "communication": f"The answer is {'well-structured and detailed' if comm_score >= 4 else 'adequate but could be more detailed' if comm_score >= 3 else 'brief and needs more elaboration'}.",
        "technical_depth": f"The response {'demonstrates strong technical knowledge' if tech_score >= 4 else 'shows some technical understanding' if tech_score >= 3 else 'lacks sufficient technical detail'}.",
        "problem_solving": f"The candidate {'effectively demonstrates problem-solving skills' if problem_score >= 4 else 'shows some problem-solving approach' if problem_score >= 3 else 'could better demonstrate problem-solving abilities'}.",
        "culture_fit": f"The answer {'shows strong collaboration and teamwork' if culture_score >= 4 else 'indicates some team orientation' if culture_score >= 3 else 'could better demonstrate teamwork'}."
    }
    
    # Generate contextual follow-up questions based on the answer
    follow_ups = []
    
    # Technical follow-up if technical content is present
    if tech_score >= 3:
        follow_ups.append("Can you dive deeper into the technical architecture and design decisions you made?")
    else:
        follow_ups.append("Can you provide more specific technical details about your implementation?")
    
    # Problem-solving follow-up
    if problem_score >= 3:
        follow_ups.append("What were the main challenges you encountered and what was your approach to solving them?")
    else:
        follow_ups.append("Can you describe a specific problem you solved and walk me through your thought process?")
    
    # Collaboration follow-up
    if culture_score >= 3:
        follow_ups.append("How did you coordinate with your team members and handle any conflicts or disagreements?")
    else:
        follow_ups.append("Can you share an example of how you collaborated with others on this project?")
    
    # Generate contextual coaching tip
    if comm_score < 3:
        coaching_tip = "Your answer could benefit from more detail. Use the STAR method (Situation, Task, Action, Result) to structure your response. Include specific examples, metrics, and outcomes."
    elif tech_score < 3 and 'engineer' in job.lower() or 'developer' in job.lower():
        coaching_tip = "For technical roles, emphasize specific technologies, tools, and methodologies you used. Include code examples, system architecture details, or performance metrics when relevant."
    elif problem_score < 3:
        coaching_tip = "Focus on demonstrating your problem-solving process. Explain the challenge clearly, describe your approach, and highlight the results or impact of your solution."
    elif culture_score < 3:
        coaching_tip = "Highlight your collaboration and teamwork skills. Mention how you worked with others, handled feedback, and contributed to team success."
    else:
        coaching_tip = "Great response! Consider adding specific metrics or quantifiable results to make your achievements even more impactful. The STAR method (Situation, Task, Action, Result) can help structure future answers."
    
    return {
        "question": question,
        "candidate_response": answer,
        "scores": {
            "communication": comm_score,
            "technical_depth": tech_score,
            "problem_solving": problem_score,
            "culture_fit": culture_score
        },
        "explanations": explanations,
        "follow_up_questions": follow_ups,
        "coaching_tip": coaching_tip
    }

