"""
DoD HFACS 7.0 — All 109 Nanocodes
Reference: Human Factors Analysis and Classification System
"""

HFACS_CODES = [
    # ==================== ACTS (10) ====================
    # Performance-Based Errors (AE100)
    {"code": "AE101", "category": "ACT", "subcategory": "Performance-Based Errors", "description": "Unintended Operation of Equipment"},
    {"code": "AE102", "category": "ACT", "subcategory": "Performance-Based Errors", "description": "Checklist Not Followed Correctly"},
    {"code": "AE103", "category": "ACT", "subcategory": "Performance-Based Errors", "description": "Procedure Not Followed Correctly"},
    {"code": "AE104", "category": "ACT", "subcategory": "Performance-Based Errors", "description": "Over-Controlled/Under-Controlled Aircraft/Vehicle"},
    {"code": "AE105", "category": "ACT", "subcategory": "Performance-Based Errors", "description": "Breakdown in Visual Scan"},
    {"code": "AE107", "category": "ACT", "subcategory": "Performance-Based Errors", "description": "Rushed or Delayed a Necessary Action"},
    # Judgment & Decision-Making Errors (AE200)
    {"code": "AE201", "category": "ACT", "subcategory": "Judgment & Decision-Making Errors", "description": "Inadequate Real-Time Risk Assessment"},
    {"code": "AE202", "category": "ACT", "subcategory": "Judgment & Decision-Making Errors", "description": "Failure to Prioritize Tasks Adequately"},
    {"code": "AE205", "category": "ACT", "subcategory": "Judgment & Decision-Making Errors", "description": "Ignored a Caution/Warning"},
    {"code": "AE206", "category": "ACT", "subcategory": "Judgment & Decision-Making Errors", "description": "Wrong Choice of Action During an Operation"},
    # Violations (AV000)
    {"code": "AV001", "category": "ACT", "subcategory": "Violations", "description": "Performs Work-Around Violation"},
    {"code": "AV002", "category": "ACT", "subcategory": "Violations", "description": "Commits Widespread/Routine Violation"},
    {"code": "AV003", "category": "ACT", "subcategory": "Violations", "description": "Extreme Violation - Lack of Discipline"},

    # ==================== PRECONDITIONS (67) ====================
    # Physical Environment (PE100)
    {"code": "PE101", "category": "PRECOND", "subcategory": "Physical Environment", "description": "Environmental Conditions Affecting Vision"},
    {"code": "PE103", "category": "PRECOND", "subcategory": "Physical Environment", "description": "Vibration Affects Vision or Balance"},
    {"code": "PE106", "category": "PRECOND", "subcategory": "Physical Environment", "description": "Heat/Cold Stress Impairs Performance"},
    {"code": "PE108", "category": "PRECOND", "subcategory": "Physical Environment", "description": "External Force or Object Impeded an Individual's Movement"},
    {"code": "PE109", "category": "PRECOND", "subcategory": "Physical Environment", "description": "Lights of Other Vehicle/Vessel/Aircraft Affected Vision"},
    {"code": "PE110", "category": "PRECOND", "subcategory": "Physical Environment", "description": "Noise Interference"},
    # Technological Environment (PE200)
    {"code": "PE201", "category": "PRECOND", "subcategory": "Technological Environment", "description": "Seat and Restraint System Problems"},
    {"code": "PE202", "category": "PRECOND", "subcategory": "Technological Environment", "description": "Instrumentation and Warning System Issues"},
    {"code": "PE203", "category": "PRECOND", "subcategory": "Technological Environment", "description": "Visibility Restrictions (not weather related)"},
    {"code": "PE204", "category": "PRECOND", "subcategory": "Technological Environment", "description": "Controls and Switches are Inadequate"},
    {"code": "PE205", "category": "PRECOND", "subcategory": "Technological Environment", "description": "Automated System Creates an Unsafe Situation"},
    {"code": "PE206", "category": "PRECOND", "subcategory": "Technological Environment", "description": "Workspace Incompatible with Operation"},
    {"code": "PE207", "category": "PRECOND", "subcategory": "Technological Environment", "description": "Personal Equipment Interference"},
    {"code": "PE208", "category": "PRECOND", "subcategory": "Technological Environment", "description": "Communication Equipment Inadequate"},
    # Physical Problem (PC300)
    {"code": "PC302", "category": "PRECOND", "subcategory": "Physical Problem", "description": "Substance Effects (alcohol, supplements, medications, drugs)"},
    {"code": "PC304", "category": "PRECOND", "subcategory": "Physical Problem", "description": "Loss of Consciousness (sudden or prolonged onset)"},
    {"code": "PC305", "category": "PRECOND", "subcategory": "Physical Problem", "description": "Physical Illness/Injury"},
    {"code": "PC307", "category": "PRECOND", "subcategory": "Physical Problem", "description": "Fatigue"},
    {"code": "PC310", "category": "PRECOND", "subcategory": "Physical Problem", "description": "Trapped Gas Disorders"},
    {"code": "PC311", "category": "PRECOND", "subcategory": "Physical Problem", "description": "Evolved Gas Disorders"},
    {"code": "PC312", "category": "PRECOND", "subcategory": "Physical Problem", "description": "Hypoxia/Hyperventilation"},
    {"code": "PC314", "category": "PRECOND", "subcategory": "Physical Problem", "description": "Inadequate Adaptation to Darkness"},
    {"code": "PC315", "category": "PRECOND", "subcategory": "Physical Problem", "description": "Dehydration"},
    {"code": "PC317", "category": "PRECOND", "subcategory": "Physical Problem", "description": "Body Size/Movement Limitations"},
    {"code": "PC318", "category": "PRECOND", "subcategory": "Physical Problem", "description": "Physical Strength & Coordination (inappropriate for task demands)"},
    {"code": "PC319", "category": "PRECOND", "subcategory": "Physical Problem", "description": "Nutrition/Diet"},
    # State of Mind (PC200)
    {"code": "PC202", "category": "PRECOND", "subcategory": "State of Mind", "description": "Psychological Problem"},
    {"code": "PC203", "category": "PRECOND", "subcategory": "State of Mind", "description": "Life Stressors"},
    {"code": "PC204", "category": "PRECOND", "subcategory": "State of Mind", "description": "Emotional State"},
    {"code": "PC205", "category": "PRECOND", "subcategory": "State of Mind", "description": "Personality Style"},
    {"code": "PC206", "category": "PRECOND", "subcategory": "State of Mind", "description": "Overconfidence"},
    {"code": "PC207", "category": "PRECOND", "subcategory": "State of Mind", "description": "Pressing"},
    {"code": "PC208", "category": "PRECOND", "subcategory": "State of Mind", "description": "Complacency"},
    {"code": "PC209", "category": "PRECOND", "subcategory": "State of Mind", "description": "Motivation"},
    {"code": "PC215", "category": "PRECOND", "subcategory": "State of Mind", "description": "Mentally Exhausted (Burnout)"},
    # Sensory Misperception (PC500)
    {"code": "PC501", "category": "PRECOND", "subcategory": "Sensory Misperception", "description": "Motion Illusion – Kinesthetic"},
    {"code": "PC502", "category": "PRECOND", "subcategory": "Sensory Misperception", "description": "Turning/Balance Illusion – Vestibular"},
    {"code": "PC503", "category": "PRECOND", "subcategory": "Sensory Misperception", "description": "Visual Illusion"},
    {"code": "PC504", "category": "PRECOND", "subcategory": "Sensory Misperception", "description": "Misperception of Changing Environment"},
    {"code": "PC505", "category": "PRECOND", "subcategory": "Sensory Misperception", "description": "Misinterpreted/Misread Instrument"},
    {"code": "PC507", "category": "PRECOND", "subcategory": "Sensory Misperception", "description": "Misinterpretation of Auditory/Sound Cues"},
    {"code": "PC508", "category": "PRECOND", "subcategory": "Sensory Misperception", "description": "Spatial Disorientation"},
    {"code": "PC511", "category": "PRECOND", "subcategory": "Sensory Misperception", "description": "Temporal/Time Distortion"},
    # Mental Awareness (PC100)
    {"code": "PC101", "category": "PRECOND", "subcategory": "Mental Awareness", "description": "Not Paying Attention"},
    {"code": "PC102", "category": "PRECOND", "subcategory": "Mental Awareness", "description": "Fixation"},
    {"code": "PC103", "category": "PRECOND", "subcategory": "Mental Awareness", "description": "Task Over-Saturation/Under-Saturation"},
    {"code": "PC104", "category": "PRECOND", "subcategory": "Mental Awareness", "description": "Confusion"},
    {"code": "PC105", "category": "PRECOND", "subcategory": "Mental Awareness", "description": "Negative Habit Transfer"},
    {"code": "PC106", "category": "PRECOND", "subcategory": "Mental Awareness", "description": "Distraction"},
    {"code": "PC107", "category": "PRECOND", "subcategory": "Mental Awareness", "description": "Geographically Lost"},
    {"code": "PC108", "category": "PRECOND", "subcategory": "Mental Awareness", "description": "Interference/Interruption"},
    {"code": "PC109", "category": "PRECOND", "subcategory": "Mental Awareness", "description": "Technical or Procedural Knowledge Not Retained after Training"},
    {"code": "PC110", "category": "PRECOND", "subcategory": "Mental Awareness", "description": "Inaccurate Expectation"},
    # Teamwork (PP100)
    {"code": "PP101", "category": "PRECOND", "subcategory": "Teamwork", "description": "Failure of Crew/Team Leadership"},
    {"code": "PP103", "category": "PRECOND", "subcategory": "Teamwork", "description": "Inadequate Task Delegation"},
    {"code": "PP104", "category": "PRECOND", "subcategory": "Teamwork", "description": "Rank/Position Intimidation"},
    {"code": "PP105", "category": "PRECOND", "subcategory": "Teamwork", "description": "Lack of Assertiveness"},
    {"code": "PP106", "category": "PRECOND", "subcategory": "Teamwork", "description": "Critical Information Not Communicated"},
    {"code": "PP107", "category": "PRECOND", "subcategory": "Teamwork", "description": "Standard/Proper Terminology Not Used"},
    {"code": "PP108", "category": "PRECOND", "subcategory": "Teamwork", "description": "Failed to Effectively Communicate"},
    {"code": "PP109", "category": "PRECOND", "subcategory": "Teamwork", "description": "Task/Mission Planning/Briefing Inadequate"},

    # ==================== SUPERVISION (15) ====================
    # Supervisory Violations (SV000)
    {"code": "SV001", "category": "SUPER", "subcategory": "Supervisory Violations", "description": "Failure to Enforce Existing Rules"},
    {"code": "SV002", "category": "SUPER", "subcategory": "Supervisory Violations", "description": "Allowing Unwritten Policies to Become Standard"},
    {"code": "SV003", "category": "SUPER", "subcategory": "Supervisory Violations", "description": "Directed Individual to Violate Existing Regulations"},
    {"code": "SV004", "category": "SUPER", "subcategory": "Supervisory Violations", "description": "Authorized Unqualified Individuals for Task"},
    # Planned Inappropriate Operations (SP000)
    {"code": "SP001", "category": "SUPER", "subcategory": "Planned Inappropriate Operations", "description": "Directed Task Beyond Personnel Capabilities"},
    {"code": "SP002", "category": "SUPER", "subcategory": "Planned Inappropriate Operations", "description": "Inappropriate Team Composition"},
    {"code": "SP003", "category": "SUPER", "subcategory": "Planned Inappropriate Operations", "description": "Selected Individual with Lack of Current or Limited Experience"},
    {"code": "SP006", "category": "SUPER", "subcategory": "Planned Inappropriate Operations", "description": "Performed Inadequate Risk Assessment – Formal"},
    {"code": "SP007", "category": "SUPER", "subcategory": "Planned Inappropriate Operations", "description": "Authorized Unnecessary Hazard"},
    # Inadequate Supervision (SI000)
    {"code": "SI001", "category": "SUPER", "subcategory": "Inadequate Supervision", "description": "Supervisory/Command Oversight Inadequate"},
    {"code": "SI002", "category": "SUPER", "subcategory": "Inadequate Supervision", "description": "Improper Role-Modeling"},
    {"code": "SI003", "category": "SUPER", "subcategory": "Inadequate Supervision", "description": "Failed to Provide Proper Training"},
    {"code": "SI004", "category": "SUPER", "subcategory": "Inadequate Supervision", "description": "Failed to Provide Appropriate Policy/Guidance"},
    {"code": "SI005", "category": "SUPER", "subcategory": "Inadequate Supervision", "description": "Personality Conflict with Supervisor"},
    {"code": "SI006", "category": "SUPER", "subcategory": "Inadequate Supervision", "description": "Lack of Supervisory Responses to Critical Information"},
    {"code": "SI007", "category": "SUPER", "subcategory": "Inadequate Supervision", "description": "Failed to Identify/Correct Risky or Unsafe Practices"},
    {"code": "SI008", "category": "SUPER", "subcategory": "Inadequate Supervision", "description": "Selected Individual with Lack of Proficiency"},

    # ==================== ORGANIZATIONAL (17) ====================
    # Resource Problems (OR000)
    {"code": "OR001", "category": "ORG", "subcategory": "Resource Problems", "description": "Command and Control Resources are Deficient"},
    {"code": "OR003", "category": "ORG", "subcategory": "Resource Problems", "description": "Inadequate Infrastructure"},
    {"code": "OR005", "category": "ORG", "subcategory": "Resource Problems", "description": "Failure to Remove Inadequate/Worn-Out Equipment in a Timely Manner"},
    {"code": "OR008", "category": "ORG", "subcategory": "Resource Problems", "description": "Failure to Provide Adequate Operational Information Resources"},
    {"code": "OR009", "category": "ORG", "subcategory": "Resource Problems", "description": "Failure to Provide Adequate Funding"},
    # Personnel Selection & Staffing (OS000)
    {"code": "OS001", "category": "ORG", "subcategory": "Personnel Selection & Staffing", "description": "Personnel Recruiting and Selection Policies are Inadequate"},
    {"code": "OS002", "category": "ORG", "subcategory": "Personnel Selection & Staffing", "description": "Failure to Provide Adequate Manning/Staffing Resources"},
    # Policy and Process Issues (OP000)
    {"code": "OP001", "category": "ORG", "subcategory": "Policy and Process Issues", "description": "Pace of Ops-tempo/Workload"},
    {"code": "OP002", "category": "ORG", "subcategory": "Policy and Process Issues", "description": "Organizational Program/Policy Risks not Adequately Assessed"},
    {"code": "OP003", "category": "ORG", "subcategory": "Policy and Process Issues", "description": "Provided Inadequate Procedural Guidance or Publications"},
    {"code": "OP004", "category": "ORG", "subcategory": "Policy and Process Issues", "description": "Organizational (formal) Training is Inadequate or Unavailable"},
    {"code": "OP005", "category": "ORG", "subcategory": "Policy and Process Issues", "description": "Flawed Doctrine/Philosophy"},
    {"code": "OP006", "category": "ORG", "subcategory": "Policy and Process Issues", "description": "Inadequate Program Management"},
    {"code": "OP007", "category": "ORG", "subcategory": "Policy and Process Issues", "description": "Purchasing or Providing Poorly Designed or Unsuitable Equipment"},
    # Climate/Culture Influences (OC000)
    {"code": "OC001", "category": "ORG", "subcategory": "Climate/Culture Influences", "description": "Organizational Climate/Culture"},
]

# Helper function to get category counts
def get_hfacs_counts():
    counts = {}
    for code in HFACS_CODES:
        counts[code["category"]] = counts.get(code["category"], 0) + 1
    return counts

# Helper function to search codes
def search_hfacs(query: str):
    query_lower = query.lower()
    return [
        code for code in HFACS_CODES
        if query_lower in code["code"].lower()
        or query_lower in code["description"].lower()
        or query_lower in code["subcategory"].lower()
    ]

# Helper function to get codes by category
def get_hfacs_by_category(category: str):
    return [code for code in HFACS_CODES if code["category"] == category]
