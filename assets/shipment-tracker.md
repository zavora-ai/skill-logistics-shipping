# Shipment Tracker Template

Use this structure when presenting shipment status updates.

---

## 🚚 {shipment_id} — {carrier_name}

**Origin:** {origin} → **Destination:** {destination} | **ETA:** {eta}

### Shipment Details

| Field | Value |
|-------|-------|
| Status | {status_emoji} {status} |
| Service | {service_level} |
| Weight | {weight_kg} kg |
| Packages | {package_count} |
| Reference | {order_reference} |

{status_emoji mapping: pending=📦, in_transit=🚚, out_for_delivery=🏃, delivered=✅, exception=🚨}

### Tracking Events

| Date | Time | Location | Event |
|------|------|----------|-------|
| {event_date} | {event_time} | {event_location} | {event_description} |

### Delivery Status

| Metric | Value |
|--------|-------|
| Days in Transit | {transit_days} |
| Promised By | {promised_date} |
| On-Time | {ontime_status} |

{if status == "exception": "🚨 Delivery exception — contact carrier immediately"}
{if transit_days > promised_days: "⚠️ Shipment delayed — notify customer"}

---

*Generated from mcp-logistics | {timestamp}*
