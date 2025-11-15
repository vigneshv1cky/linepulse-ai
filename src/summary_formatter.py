def format_kpis_for_llm(kpis: dict) -> str:
    lines = []
    lines.append(
        f"Total downtime: {kpis['total_downtime_minutes']:.1f} minutes "
        f"({kpis['total_downtime_hours']:.2f} hours) "
        f"between {kpis['date_range']['min_date']} and {kpis['date_range']['max_date']}."
    )

    if "downtime_by_type" in kpis:
        lines.append("\nTop downtime types (by minutes):")
        for t, mins in sorted(kpis["downtime_by_type"].items(), key=lambda x: x[1], reverse=True)[:5]:
            lines.append(f"  - {t}: {mins:.1f} minutes")

    if "downtime_by_machine" in kpis:
        lines.append("\nMachines with highest downtime:")
        for m, mins in sorted(kpis["downtime_by_machine"].items(), key=lambda x: x[1], reverse=True)[:5]:
            lines.append(f"  - {m}: {mins:.1f} minutes")

    if "downtime_by_location" in kpis:
        lines.append("\nLocations with highest downtime:")
        for loc, mins in sorted(kpis["downtime_by_location"].items(), key=lambda x: x[1], reverse=True)[:5]:
            lines.append(f"  - {loc}: {mins:.1f} minutes")

    if "planned_vs_unplanned" in kpis:
        pv = kpis["planned_vs_unplanned"]
        lines.append(
            f"\nPlanned vs unplanned downtime (minutes): "
            f"planned = {pv['planned_minutes']:.1f}, "
            f"unplanned = {pv['unplanned_minutes']:.1f}."
        )

    if "top_causes" in kpis:
        lines.append("\nTop downtime causes:")
        for cause, mins in kpis["top_causes"].items():
            short = (cause[:120] + "...") if len(cause) > 120 else cause
            lines.append(f"  - {mins:.1f} min → {short}")

    return "\n".join(lines)
