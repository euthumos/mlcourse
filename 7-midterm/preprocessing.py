def feature_eng(data):
    data["BMI"] = data["weight(kg)"] / (data["height(cm)"]/100)**2
    data["HDL-LDL Ratio"] = data["HDL"] / data["LDL"]
    data["HDL-triglyceride Ratio"] = data["HDL"] / data["triglyceride"]
    data["LDL-triglyceride Ratio"] = data["LDL"] / data["triglyceride"]
    data["Liver Enzyme Ratio"] = data["AST"] / data["ALT"]