import pandas as pd


def load_and_prepare(file) -> pd.DataFrame:
    df = pd.read_csv(file)

    # Parse dates
    df["downtime_start"] = pd.to_datetime(df["downtime_start"], errors="coerce")
    df["downtime_end"] = pd.to_datetime(df["downtime_end"], errors="coerce")
    df["report_date"] = pd.to_datetime(df["report_date"], errors="coerce").dt.date

    # Duration
    df["duration_minutes"] = pd.to_numeric(df["duration_minutes"], errors="coerce")
    df = df.dropna(subset=["downtime_start", "duration_minutes"])

    # Text fields
    text_cols = [
        "downtime_type",
        "cause_description",
        "machine_name",
        "machine_id",
        "location",
        "production_impact",
        "resolved_by",
        "parts_replaced",
        "reported_by",
    ]
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].fillna("")

    # Boolean
    if "scheduled_maintenance" in df.columns:
        df["scheduled_maintenance"] = df["scheduled_maintenance"].astype(bool)

    return df
