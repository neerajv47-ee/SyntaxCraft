"""
SyntaxCraft - Beginner-Focused Python Learning Platform
Main Application Entry Point (Integrated MVP)

Author: SyntaxCraft Team
Framework: Flask
"""

import json
import os
from flask import Flask, render_template, request, jsonify, session
from generator import generate_code, SUPPORTED_TASKS
from insights import analyze_code
from testing import generate_test_cases
from history import add_history, get_history, clear_history
from data.python_hub_data import HUB_TOPICS

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = "syntaxcraft-presentation-ready-secret-key-2026"

# Base directory path for resolving project assets
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "problems.json")


def load_problems():
    """Load practice problems from the local JSON storage file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


# ---------------------------------------------------------------------------
# 1. Home Route
# ---------------------------------------------------------------------------

@app.route("/")
def home():
    """Home Page: Introduction, overview, and quick-access feature cards."""
    return render_template("index.html", active_page="home")


# ---------------------------------------------------------------------------
# 2. Code Generator Route (Core Engine)
# ---------------------------------------------------------------------------

@app.route("/generator", methods=["GET", "POST"])
def generator():
    """
    Code Generator: Translates plain English instructions into clean Python code.
    Supports both standard Form POST and AJAX JSON requests.
    Persists generation into local SQLite history and session context.
    """
    user_prompt = ""
    difficulty = "Beginner"
    generated_result = None

    if request.method == "POST":
        try:
            if request.is_json:
                data = request.get_json() or {}
                user_prompt = data.get("prompt", "")
                difficulty = data.get("difficulty", "Beginner")
                generated_result = generate_code(user_prompt, difficulty)

                # Persist to local history and session if successful
                if generated_result.get("success"):
                    task_id = generated_result.get("task_id")
                    task_name = generated_result.get("task")
                    code = generated_result.get("code")
                    session["last_task_id"] = task_id
                    session["last_task_name"] = task_name
                    session["last_difficulty"] = difficulty
                    session["last_code"] = code
                    session["last_prompt"] = user_prompt
                    add_history(user_prompt, difficulty, task_name, code)

                return jsonify(generated_result)

            # Standard Form Submission
            user_prompt = request.form.get("prompt", "")
            difficulty = request.form.get("difficulty", "Beginner")
            generated_result = generate_code(user_prompt, difficulty)

            if generated_result.get("success"):
                task_id = generated_result.get("task_id")
                task_name = generated_result.get("task")
                code = generated_result.get("code")
                session["last_task_id"] = task_id
                session["last_task_name"] = task_name
                session["last_difficulty"] = difficulty
                session["last_code"] = code
                session["last_prompt"] = user_prompt
                add_history(user_prompt, difficulty, task_name, code)

        except Exception as exc:
            generated_result = {
                "success": False,
                "task": None,
                "task_id": None,
                "difficulty": difficulty,
                "code": "Sorry, an unexpected error occurred during code generation. Please try again.",
                "message": str(exc)
            }

    return render_template(
        "generator.html",
        active_page="generator",
        user_prompt=user_prompt,
        difficulty=difficulty,
        generated_result=generated_result
    )


# ---------------------------------------------------------------------------
# 3. Code Insights Route
# ---------------------------------------------------------------------------

@app.route("/insights")
def insights():
    """
    Code Insights: Static source analysis and line-by-line explanation.
    Seamlessly inherits the code generated in the Code Generator or allows
    inspecting any of the 15 tasks via task selector.
    """
    # Check query parameters first, then session context, then fallback
    task_id = request.args.get("task") or session.get("last_task_id") or "largest_of_three"
    difficulty = request.args.get("difficulty") or session.get("last_difficulty") or "Beginner"
    code = session.get("last_code") or ""

    # Generate insights metadata
    insight_data = analyze_code(code, task_id, difficulty)

    return render_template(
        "insights.html",
        active_page="insights",
        insight=insight_data,
        all_tasks=SUPPORTED_TASKS,
        current_task_id=task_id,
        current_difficulty=difficulty
    )


# ---------------------------------------------------------------------------
# 4. Test Cases Route
# ---------------------------------------------------------------------------

@app.route("/test-cases")
def test_cases():
    """
    Test Cases: Validates solutions against multiple input/output test cases.
    Directly connected to the generated code and task context.
    """
    task_id = request.args.get("task") or session.get("last_task_id") or "largest_of_three"
    difficulty = request.args.get("difficulty") or session.get("last_difficulty") or "Beginner"

    test_data = generate_test_cases(task_id, difficulty)

    return render_template(
        "test_cases.html",
        active_page="test_cases",
        test_data=test_data,
        all_tasks=SUPPORTED_TASKS,
        current_task_id=task_id,
        current_difficulty=difficulty
    )


# ---------------------------------------------------------------------------
# 5. Practice Mode Routes
# ---------------------------------------------------------------------------

@app.route("/practice")
def practice():
    """Practice Mode: Curated interactive beginner challenges."""
    problems = load_problems()
    return render_template("practice.html", active_page="practice", problems=problems)


@app.route("/api/check-practice", methods=["POST"])
def check_practice():
    """
    Safe rule-based checking for Practice Mode challenges.
    Evaluates student code against expected structural requirements without eval/exec.
    """
    data = request.get_json() or {}
    problem_id = data.get("problem_id", "")
    user_code = data.get("code", "")

    problems = load_problems()
    problem = next((p for p in problems if p["id"] == problem_id), None)

    if not problem:
        return jsonify({"success": False, "message": "Problem not found."}), 404

    if not user_code or len(user_code.strip()) < 8:
        return jsonify({
            "success": True,
            "correct": False,
            "message": "✗ Incorrect",
            "explanation": "Please write your Python solution code in the editor before checking."
        })

    # Rule-based validation: check presence of required keywords / syntax elements
    expected_keywords = problem.get("expected_keywords", [])
    code_lower = user_code.lower()

    # Check that required logic markers are present
    matches = [kw for kw in expected_keywords if kw.lower() in code_lower]
    # If majority of required logical markers exist, mark correct
    is_correct = len(matches) >= max(1, len(expected_keywords) - 1)

    if is_correct:
        return jsonify({
            "success": True,
            "correct": True,
            "message": "✓ Correct",
            "explanation": problem.get("explanation", "Great job! Your solution meets all structural requirements.")
        })
    else:
        return jsonify({
            "success": True,
            "correct": False,
            "message": "✗ Incorrect",
            "explanation": f"Make sure your logic handles the problem requirements using {', '.join(expected_keywords[:3])}."
        })


# ---------------------------------------------------------------------------
# 6. Python Hub Route
# ---------------------------------------------------------------------------

@app.route("/python-hub")
def python_hub():
    """Python Hub: 17 student-tailored reference topics and cheat sheets."""
    return render_template("python_hub.html", active_page="python_hub", topics=HUB_TOPICS)


# ---------------------------------------------------------------------------
# 7. History Route & Management
# ---------------------------------------------------------------------------

@app.route("/history")
def history():
    """History: Displays previous English-to-Python generations from local SQLite."""
    history_records = get_history()
    return render_template("history.html", active_page="history", records=history_records)


@app.route("/api/clear-history", methods=["POST"])
def clear_history_api():
    """Clear local history database records."""
    clear_history()
    return jsonify({"success": True, "message": "History cleared successfully."})


# ---------------------------------------------------------------------------
# Application Runner
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("  SyntaxCraft Server Running")
    print("  Access platform: http://127.0.0.1:5000")
    print("=" * 50 + "\n")
    app.run(debug=True, host="127.0.0.1", port=5000)
