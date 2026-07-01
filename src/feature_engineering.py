def create_features(master):

    master["Hour"] = master["Timestamp"].dt.hour

    master["Month"] = master["Timestamp"].dt.month

    master["Weekend"] = (
        master["Timestamp"].dt.dayofweek >= 5
    ).astype(int)

    return master