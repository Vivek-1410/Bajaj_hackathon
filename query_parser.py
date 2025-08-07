# query_parser.py

def parse_query(user_input):
    
    import re
    age = int(re.search(r"\d+", user_input).group())
    gender = "male" if "male" in user_input.lower() else "female"
    procedure = "knee surgery" if "knee" in user_input.lower() else "unknown"
    location = "Pune" if "Pune" in user_input else "unknown"
    policy_duration = "3 months" if "3-month" in user_input else "unknown"

    return {
        "age": age,
        "gender": gender,
        "procedure": procedure,
        "location": location,
        "policy_duration": policy_duration
    }
