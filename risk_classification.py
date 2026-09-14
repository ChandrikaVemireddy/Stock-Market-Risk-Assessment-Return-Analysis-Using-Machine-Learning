def assign_risk(volatility, low_threshold, high_threshold):
    if volatility != volatility:
        return None
    if volatility <= low_threshold:
        return 'Low Risk'
    if volatility <= high_threshold:
        return 'Medium Risk'
    return 'High Risk'
