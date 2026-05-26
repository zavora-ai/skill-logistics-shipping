# Logistics Cross-MCP Workflows

## Logistics + ERP: Order Fulfillment
```
ERP: get_sales_order(id: "SO-001") → {items: [...], ship_to: address}
LOGISTICS: validate_address(address) → valid ✅
LOGISTICS: get_rates(from: warehouse, to: customer) → cheapest $12.50
LOGISTICS: book_rate(rate_id) → {tracking: "1Z999..."}
LOGISTICS: generate_label(shipment_id)
ERP: update_sales_order(id: "SO-001", status: "shipped", tracking: "1Z999...")
EMAIL: send_email(to: customer, subject: "Your order shipped!", body: "Track: 1Z999...")
```

## Logistics + Notifications: Delivery Alerts
```
LOGISTICS: track_shipment(tracking) → {status: "delivered"}
NOTIFICATIONS: send_notification(recipient: customer, title: "📦 Delivered!", body: "Your package was delivered at 2:30 PM")
CRM: create_activity(type: "note", subject: "Order delivered to customer")
```

## Logistics + Slack: Shipping Exceptions
```
LOGISTICS: get_tracking_events(tracking) → {exception: "Address not found"}
SLACK: send_message(channel: "#fulfillment", text: "⚠️ Shipping exception: 1Z999... — address not found. Customer: Acme Corp. Action needed.")
```
