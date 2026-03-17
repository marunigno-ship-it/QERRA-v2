from vectors_bridge import get_ethical_confidence_modifier, v008_example

def get_ethical_decision(base_confidence, region_threshold=0.85):
    bonus = get_ethical_confidence_modifier(v008_example)
    final_conf = base_confidence + bonus
    if final_conf >= region_threshold:
        return "ALLOWED", f"v008 ethics boosted to {final_conf:.2f} (threshold {region_threshold})"
    else:
        return "HALTED", f"v008 ethics insufficient: {final_conf:.2f} < {region_threshold}"

# Quick test (can be removed later)
if __name__ == "__main__":
    decision, reason = get_ethical_decision(0.82)
    print("Decision:", decision, "| Reason:", reason)
    # Next: integrate this decision helper into start.py for full kernel + ethics flow