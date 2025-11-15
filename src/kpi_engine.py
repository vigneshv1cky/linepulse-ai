import pandas as pd


def compute_kpis(df: pd.DataFrame) -> dict:
    kpis = {}
    total_minutes = df["duration_minutes"].sum()
    kpis["total_downtime_minutes"] = float(total_minutes)
    kpis["total_downtime_hours"] = float(total_minutes / 60.0)

    kpis["date_range"] = {
        "min_date": df["downtime_start"].min().strftime("%Y-%m-%d"),
        "max_date": df["downtime_start"].max().strftime("%Y-%m-%d"),
    }

    if "downtime_type" in df.columns:
        dt = df.groupby("downtime_type")["duration_minutes"].sum().sort_values(ascending=False)
        kpis["downtime_by_type"] = dt.to_dict()

    if "machine_name" in df.columns:
        dm = df.groupby("machine_name")["duration_minutes"].sum().sort_values(ascending=False)
        kpis["downtime_by_machine"] = dm.to_dict()

    if "location" in df.columns:
        dl = df.groupby("location")["duration_minutes"].sum().sort_values(ascending=False)
        kpis["downtime_by_location"] = dl.to_dict()

    if "scheduled_maintenance" in df.columns:
        planned = df[df["scheduled_maintenance"]]["duration_minutes"].sum()
        unplanned = df[~df["scheduled_maintenance"]]["duration_minutes"].sum()
        kpis["planned_vs_unplanned"] = {"planned_minutes": float(planned), "unplanned_minutes": float(unplanned)}

    if "cause_description" in df.columns:
        causes = df.groupby("cause_description")["duration_minutes"].sum().sort_values(ascending=False).head(5)
        kpis["top_causes"] = causes.to_dict()

    return kpis
