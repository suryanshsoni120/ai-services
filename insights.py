def generate_insights(summary, breakdown, alerts):
    insights = []

    income = summary.get("income", 0)
    expense = summary.get("expense", 0)
    savings = summary.get("savings", 0)

    # Overall summary
    if expense > income:
        insights.append(
            f"Your expenses exceeded income this month, resulting in a deficit of ₹{abs(savings)}."
        )
    else:
        insights.append(
            f"You saved ₹{savings} this month. Good job managing your finances."
        )

    # Category insights
    if breakdown:
        top_category = breakdown[0]
        insights.append(
            f"Your highest spending was on {top_category['_id']} at ₹{top_category['total']}."
        )

    # Budget alerts
    for alert in alerts:
        if alert["type"] == "OVERALL":
            insights.append(
                "You crossed your overall monthly budget. Consider cutting down discretionary expenses."
            )
        if alert["type"] == "CATEGORY":
            insights.append(
                f"You overspent in the {alert['category']} category. Monitor this category closely."
            )

    return insights