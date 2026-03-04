import os
import sys
import json
import argparse
import re

def update_memo(v1_memo, onboarding_text):
    v2_memo = v1_memo.copy()
    text = onboarding_text
    changes = []
    
    # helper for updates
    def record_change(field, new_val, label):
        old = v2_memo.get(field)
        if new_val and new_val != old:
            v2_memo[field] = new_val
            changes.append(f"- Updated {label}: {new_val}")
            return True
        return False

    # 1. Company Name (if changed/refined)
    name_match = re.search(r"(?:officially it's|company name is) ([\w\s]+?)(?:[\.,]|$)", text, re.IGNORECASE)
    if name_match:
        record_change("company_name", name_match.group(1).strip(), "Company Name")

    # 2. Business Hours
    hours_match = re.search(r"(?:hours are|open) ([\w\s,]+?) (?:from|between) (\d{1,2}(?::\d{2})?\s*[ap]m) (?:to|until) (\d{1,2}(?::\d{2})?\s*[ap]m)", text, re.IGNORECASE)
    if hours_match:
        record_change("business_hours", f"{hours_match.group(1).strip()}: {hours_match.group(2)} - {hours_match.group(3)}", "Business Hours")

    # 3. Address
    addr_match = re.search(r"(?:located at|address is) ([\w\s,]+?)(?:[\.!]|$)", text, re.IGNORECASE)
    if addr_match:
        record_change("office_address", addr_match.group(1).strip(), "Office Address")
        
    # 4. Emergency definitions
    emerg_match = re.search(r"(?:emergency is strictly when|emergencies include|consider it an emergency ONLY if|qualifies as an emergency if) (.*?\.)", text, re.IGNORECASE)
    if emerg_match:
        v2_memo["emergency_definition"] = [emerg_match.group(1).strip()]
        changes.append(f"- Updated Emergency Definition: {v2_memo['emergency_definition'][0]}")
        
    # 5. Emergency routing
    e_route_match = re.search(r"transfer (?:the call|emergency calls)(?: directly)? to ([\w\s]+) at ([\d\-]+)", text, re.IGNORECASE)
    if e_route_match:
        new_rule = f"Transfer to {e_route_match.group(1).strip()} at {e_route_match.group(2)}"
        record_change("emergency_routing_rules", new_rule, "Emergency Routing Rules")
        
    # 6. Non-emergency routing
    non_emerg_match = re.search(r"(?:for non-emergencies|non-emergency calls)[,]* (.*?\.)", text, re.IGNORECASE)
    if non_emerg_match:
        record_change("non_emergency_routing_rules", non_emerg_match.group(1).strip(), "Non-Emergency Routing Rules")
        
    # 7. Integration / Constraints
    if "integration" in text.lower() or "integrate" in text.lower():
        confirm_match = re.search(r"(?:confirm|confirmed) we (?:can|should) integrate with ([\w\s]+)", text, re.IGNORECASE)
        if confirm_match:
            v2_memo["integration_constraints"] = f"Integrate with {confirm_match.group(1).strip()}"
            changes.append(f"- Confirmed Integration: {v2_memo['integration_constraints']}")

    # 8. Clear unknowns
    v2_memo["questions_or_unknowns"] = []
    changes.append("- Cleared prior questions_or_unknowns as onboarding is complete")

    return v2_memo, "\n".join(changes)

def main():
    parser = argparse.ArgumentParser(description="Patch v1 Memo with Onboarding Input using Rules")
    parser.add_argument("v1_memo_path", help="Path to the v1 JSON memo")
    parser.add_argument("onboarding_input_path", help="Path to the onboarding transcript text")
    parser.add_argument("output_memo_path", help="Path to save the v2 JSON memo")
    parser.add_argument("output_changelog_path", help="Path to save changes.md")
    args = parser.parse_args()

    try:
        with open(args.v1_memo_path, 'r', encoding='utf-8') as f:
            v1_memo_data = json.load(f)
            
        with open(args.onboarding_input_path, 'r', encoding='utf-8') as f:
            onboarding_input = f.read()
    except Exception as e:
        print(f"Error reading files: {e}", file=sys.stderr)
        sys.exit(1)

    print("Diffing and generating v2 memo using rule-based parsing...")
    
    v2_memo, changelog = update_memo(v1_memo_data, onboarding_input)
    
    output_dir = os.path.dirname(args.output_memo_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(args.output_memo_path, 'w', encoding='utf-8') as f:
        json.dump(v2_memo, f, indent=4)
        
    changelog_dir = os.path.dirname(args.output_changelog_path)
    if changelog_dir:
        os.makedirs(changelog_dir, exist_ok=True)
    with open(args.output_changelog_path, 'w', encoding='utf-8') as f:
        f.write("# Changelog v1 to v2\n" + changelog + "\n")
        
    print(f"v2 Memo saved to {args.output_memo_path}")
    print(f"Changelog saved to {args.output_changelog_path}")

if __name__ == "__main__":
    main()
