import plotly.express as px


def downtime_by_type_chart(kpis: dict):
    if "downtime_by_type" not in kpis:
        return px.bar(title="No downtime_type data")
    data = kpis["downtime_by_type"]
    return px.bar(
        x=list(data.keys()),
        y=list(data.values()),
        labels={"x": "Downtime Type", "y": "Minutes"},
        title="Downtime by Type",
    )


def downtime_by_machine_chart(kpis: dict):
    if "downtime_by_machine" not in kpis:
        return px.bar(title="No machine_name data")
    data = kpis["downtime_by_machine"]
    return px.bar(
        x=list(data.keys()), y=list(data.values()), labels={"x": "Machine", "y": "Minutes"}, title="Downtime by Machine"
    )
