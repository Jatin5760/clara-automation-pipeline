import os
import sys
import json
import argparse

def generate_spec_from_template(memo, version):
    company = memo.get("company_name", "the business")
    services = ", ".join(memo.get("services_supported", []))
    hours_info = memo.get("business_hours")
    
    if isinstance(hours_info, dict):
        hours_str = f"{hours_info.get('days', '')} {hours_info.get('start', '')} to {hours_info.get('end', '')} {hours_info.get('timezone', '')}".strip()
    elif isinstance(hours_info, str):
        hours_str = hours_info
    else:
        hours_str = "Unknown"
        
    address = memo.get("office_address", "Unknown")
    emergency_rule = memo.get('emergency_routing_rules', 'Escalate immediately')
    
    # Rubric-compliant System Prompt Template
    system_prompt = f"""You are Clara, the AI answering agent for {company}.

# Core Identity & Tone
- Persona: Friendly, professional, and confident.
- Tone: Helpful and reliable. DO NOT sound robotic or mention "function calls".

# Business Hours Flow ({hours_str})
1. Greeting: Greet the caller and state your purpose.
2. Purpose: Identify the reason for the call.
3. Collection: Safely collect the caller's Name and Phone Number.
4. Route/Transfer: Attempt transfer to the appropriate department if required.
5. Fallback: If transfer fails or no one is available, apologize, collect a message.
6. Verification: Confirm next steps with the caller.
7. Closing: Ask if there is "anything else" and close the call professionally.

# After Hours Flow
1. Greeting: Greet the caller and state you are the after-hours assistant.
2. Purpose: State that you are here to assist with urgent needs.
3. Emergency Check: Confirm if the situation is an EMERGENCY (Flood, Fire, Total Loss of Service).
4. If EMERGENCY: Collect Name, Phone Number, and Address immediately. Attempt transfer to on-call tech.
5. If NON-EMERGENCY: Take a message and assure them of a quick follow-up the next business morning.
6. Fallback: If any transfer fails, assure the caller of a manual follow-up.
7. Closing: Ask if there is "anything else" and close the call professionally.

# Routing Rules
- Emergency: {emergency_rule}
- Non-Emergency: {memo.get('non_emergency_routing_rules', 'Take message for office')}
- Services Supported: {services}

# Constraints
- Business Hours: {hours_str}
- Office Address: {address}
- Integration: {memo.get('integration_constraints', 'None specified')}
"""

    spec = {
        "agent_name": f"Clara for {company}",
        "version": version,
        "voice_style": "Friendly, professional, and confident.",
        "system_prompt": system_prompt.strip(),
        "key_variables": {
            "timezone": hours_info.get("timezone", "Unknown") if isinstance(hours_info, dict) else "Unknown",
            "business_hours": hours_str,
            "address": address,
            "emergency_routing": emergency_rule
        },
        "tool_invocation_placeholders": ["transfer_call", "check_calendar", "create_note"],
        "call_transfer_protocol": memo.get("call_transfer_rules", "Transfer, then fallback to message if no answer."),
        "fallback_protocol": "If transfer fails, apologize, collect callback number, and confirm follow-up."
    }
    return spec

def main():
    parser = argparse.ArgumentParser(description="Generate Retell Agent Spec via Templates")
    parser.add_argument("memo_path", help="Path to input JSON memo")
    parser.add_argument("version", help="Version, e.g., 'v1' or 'v2'")
    parser.add_argument("output_path", help="Path to save output JSON agent spec")
    args = parser.parse_args()

    try:
        with open(args.memo_path, 'r', encoding='utf-8') as f:
            memo_data = json.load(f)
    except Exception as e:
        print(f"Error reading memo: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Generating templated agent spec version {args.version}...")
    spec = generate_spec_from_template(memo_data, args.version)
    
    output_dir = os.path.dirname(args.output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        
    with open(args.output_path, 'w', encoding='utf-8') as f:
        json.dump(spec, f, indent=4)
        
    print(f"Agent Spec saved to {args.output_path}")

if __name__ == "__main__":
    main()
