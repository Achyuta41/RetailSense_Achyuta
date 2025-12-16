## Forecast Output Schema
{
  "product": string,
  "avg_daily_demand": number,
  "forecast_horizon_days": number
}

## Inventory Alert Schema
{
  "product": string,
  "current_stock": number,
  "days_left": number,
  "severity": "LOW" | "MEDIUM" | "HIGH"
}

## Sales Summary Schema
{
  "product": string,
  "avg_daily_sales": number,
  "sales_status": "LOW_SALES" | "NORMAL"
}

## Offer Schema
{
  "product": string,
  "discount": number,
  "priority": "LOW" | "MEDIUM" | "HIGH",
  "reason": string
}

## Orchestrator Output Schema
{
  "inventory_alerts": InventoryAlert[],
  "sales_summary": SalesSummary[],
  "offers": Offer[]
}
