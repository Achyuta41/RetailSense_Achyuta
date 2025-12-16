class Orchestrator:
    def run(self):
        # MOCK DATA (agents not integrated yet)

        inventory_alerts = [
            {
                "product": "Rice",
                "current_stock": 10,
                "days_left": 2,
                "severity": "HIGH"
            }
        ]

        sales_summary = [
            {
                "product": "Rice",
                "avg_daily_sales": 2.5,
                "sales_status": "LOW_SALES"
            }
        ]

        offers = [
            {
                "product": "Rice",
                "discount": 20,
                "priority": "HIGH",
                "reason": "Low sales and low stock"
            }
        ]

        return {
            "inventory_alerts": inventory_alerts,
            "sales_summary": sales_summary,
            "offers": offers
        }
