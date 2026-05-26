#!/usr/bin/env python3
"""Basic address validation before shipping."""
import json, sys, re

def validate(addr):
    result = {"valid": True, "errors": [], "warnings": []}
    if not addr.get("street"):
        result["valid"] = False
        result["errors"].append("Street address required")
    if not addr.get("city"):
        result["valid"] = False
        result["errors"].append("City required")
    if not addr.get("country"):
        result["valid"] = False
        result["errors"].append("Country code required")
    country = addr.get("country", "").upper()
    if len(country) != 2:
        result["valid"] = False
        result["errors"].append("Country must be 2-letter ISO code")
    if country in ("US", "CA") and not addr.get("postal_code"):
        result["valid"] = False
        result["errors"].append("Postal code required for US/CA")
    if country == "US" and addr.get("postal_code") and not re.match(r'^\d{5}(-\d{4})?$', addr["postal_code"]):
        result["warnings"].append("US postal code format should be XXXXX or XXXXX-XXXX")
    return result

if __name__ == "__main__":
    print(json.dumps(validate(json.loads(sys.argv[1])), indent=2))
