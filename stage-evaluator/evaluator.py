#!/usr/bin/env python3
"""
Stage Evaluator CLI - Mastery and Proof Verification Engine
Part of the Farbod 24-Month AI Execution Blueprint
"""

import argparse
import json
import os
import sys
import unittest
from datetime import datetime
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = Path(__file__).parent.resolve()
LEDGER_FILE = BASE_DIR / "mastery_ledger.json"

STAGES = {
    0: {
        "name": "Stage 0: پایتون پیشرفته و تفکر مهندسی",
        "en_name": "Advanced Python and Engineering Mindset",
        "test_module": "tests.test_stage_0",
        "badge": "Python Systems Specialist",
        "gate": "Gate 0 (Day 7)",
    },
    1: {
        "name": "Stage 1: بک‌اند پروداکشن، داکر و دیتابیس",
        "en_name": "Production Backend, Docker and SQL",
        "test_module": "tests.test_stage_1",
        "badge": "Production Backend Engineer",
        "gate": "Gate 1 (Week 8 - P0)",
    },
    2: {
        "name": "Stage 2: آمار کاربردی و یادگیری ماشین کلاسیک",
        "en_name": "Applied Stats and Classical ML",
        "test_module": "tests.test_stage_2",
        "badge": "Applied ML Practitioner",
        "gate": "Gate 2 (Week 16 - P1)",
    },
    3: {
        "name": "Stage 3: یادگیری عمیق، مدل‌های محلی و RAG سازمانی",
        "en_name": "Deep Learning, Local LLMs and RAG",
        "test_module": "tests.test_stage_3",
        "badge": "Enterprise RAG Architect",
        "gate": "Gate 3 (Week 32 - P2)",
    },
    4: {
        "name": "Stage 4: سیستم‌های ایجنتی و پروتکل MCP",
        "en_name": "Agentic AI and Model Context Protocol",
        "test_module": "tests.test_stage_4",
        "badge": "Agentic Systems Developer",
        "gate": "Gate 4 (Week 40 - P3)",
    },
    5: {
        "name": "Stage 5: هوش چندرسانه‌ای و پردازش صوت/ویدیو",
        "en_name": "Multimodal Video and Audio AI",
        "test_module": "tests.test_stage_5",
        "badge": "Multimodal Creative AI Specialist",
        "gate": "Gate 4 (Week 48 - P4)",
    },
    6: {
        "name": "Stage 6: پایلوت واقعی، مانیتورینگ و استانداردهای صنعتی",
        "en_name": "Real-World Pilot and Production Reliability",
        "test_module": "tests.test_stage_6",
        "badge": "AI Systems Reliability Master",
        "gate": "Gate 5 (Month 12 - P5)",
    },
}

def load_ledger():
    if LEDGER_FILE.exists():
        try:
            with open(LEDGER_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"stages": {}, "history": [], "last_updated": None}

def save_ledger(ledger):
    ledger["last_updated"] = datetime.now().isoformat()
    with open(LEDGER_FILE, "w", encoding="utf-8") as f:
        json.dump(ledger, f, ensure_ascii=False, indent=2)

def run_stage_tests(stage_num):
    if stage_num not in STAGES:
        print(f"[-] Invalid stage number: {stage_num}")
        return False, 0, 0

    stage_info = STAGES[stage_num]
    test_module_name = stage_info["test_module"]

    print("\n" + "="*65)
    print(f"[*] Evaluating: {stage_info['name']}")
    print(f"[*] Gate: {stage_info['gate']} | Badge: {stage_info['badge']}")
    print("="*65)

    sys.path.insert(0, str(BASE_DIR))
    loader = unittest.TestLoader()
    try:
        suite = loader.loadTestsFromName(test_module_name)
    except Exception as e:
        print(f"[-] Error loading test suite {test_module_name}: {e}")
        return False, 0, 0

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    total_tests = result.testsRun
    failed_tests = len(result.failures) + len(result.errors)
    passed_tests = total_tests - failed_tests
    success = (failed_tests == 0 and total_tests > 0)

    score_pct = round((passed_tests / total_tests) * 100, 1) if total_tests > 0 else 0

    ledger = load_ledger()
    stage_key = f"stage_{stage_num}"
    ledger["stages"][stage_key] = {
        "passed": success,
        "score_pct": score_pct,
        "passed_tests": passed_tests,
        "total_tests": total_tests,
        "last_evaluated": datetime.now().isoformat(),
        "badge": stage_info["badge"] if success else None,
    }
    ledger["history"].append({
        "stage": stage_num,
        "timestamp": datetime.now().isoformat(),
        "score_pct": score_pct,
        "passed": success,
    })
    save_ledger(ledger)

    if success:
        print(f"\n[+] CONGRATULATIONS! Stage {stage_num} PASSED with 100% score!")
        print(f"[+] Verified Proof Badge Awarded: [{stage_info['badge']}]")
    else:
        print(f"\n[-] Stage {stage_num} FAILED: {passed_tests}/{total_tests} passed ({score_pct}%).")
        print(f"[-] Check the assertion errors above and update your implementation in challenges/.")

    return success, passed_tests, total_tests

def print_status():
    ledger = load_ledger()
    print("\n" + "="*70)
    print("          AI MASTERY STAGE EVALUATION SCORECARD")
    print("="*70)
    print(f"Stage    | Status     | Score    | Gate                 | Badge")
    print("-" * 70)

    total_passed = 0
    for num, info in STAGES.items():
        stage_key = f"stage_{num}"
        data = ledger["stages"].get(stage_key, {})
        passed = data.get("passed", False)
        score = f"{data.get('score_pct', 0)}%" if "score_pct" in data else "N/A"
        status_str = "[PASS]" if passed else ("[FAIL]" if "score_pct" in data else "[PENDING]")
        badge_str = info["badge"] if passed else "-"
        if passed:
            total_passed += 1

        print(f"{num:<8} | {status_str:<10} | {score:<8} | {info['gate']:<20} | {badge_str}")

    print("-" * 70)
    print(f"Overall Mastery Progress: {total_passed}/{len(STAGES)} stages verified.")
    print("=" * 70 + "\n")

def main():
    parser = argparse.ArgumentParser(description="AI Roadmap Stage Evaluator CLI")
    parser.add_argument("--stage", "-s", type=int, choices=list(STAGES.keys()), help="Stage number to test (0 to 6)")
    parser.add_argument("--all", "-a", action="store_true", help="Run tests for all stages")
    parser.add_argument("--status", action="store_true", help="Display current mastery ledger scorecard")
    args = parser.parse_args()

    if args.status or (args.stage is None and not args.all):
        print_status()
        return

    if args.stage is not None:
        run_stage_tests(args.stage)
    elif args.all:
        for num in STAGES.keys():
            run_stage_tests(num)
        print_status()

if __name__ == "__main__":
    main()
