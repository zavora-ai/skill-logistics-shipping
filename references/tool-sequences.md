# Logistics Tool Sequences

## Tools (16)
| Tool | Purpose |
|------|---------|
| `create_shipment` | Create shipment record |
| `list_shipments` | All shipments |
| `get_shipment` | Shipment details |
| `cancel_shipment` | Cancel before pickup |
| `get_rates` | Carrier rate quotes |
| `compare_rates` | Rank by cost/speed |
| `list_carriers` | Available carriers |
| `book_rate` | Book selected rate |
| `track_shipment` | Current status |
| `get_tracking_events` | Full event history |
| `generate_label` | Shipping label |
| `get_label` | Download label |
| `validate_address` | Verify deliverability |
| `optimize_route` | Multi-stop optimization |
| `get_eta` | Estimated delivery |
| `get_distance` | Distance calculation |

## Sequence: Ship Package (5 calls)
```
1. validate_address(address) → {valid: true, standardized: "..."}
2. get_rates(from, to, weight, dimensions) → [{carrier: "FedEx", cost: 1250, days: 2}, ...]
3. compare_rates(rates) → cheapest: FedEx $12.50, fastest: UPS $18.00 (1 day)
4. book_rate(rate_id: "fedex_ground") → {shipment_id: "shp_123"}
5. generate_label(shipment_id: "shp_123") → {label_url: "..."}
```

## Sequence: Track (2 calls)
```
1. track_shipment(tracking: "1Z999...") → {status: "in_transit", location: "Memphis, TN"}
2. get_eta(tracking: "1Z999...") → {estimated: "2025-01-20", confidence: "high"}
```
