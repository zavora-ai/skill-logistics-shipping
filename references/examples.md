# Logistics Examples

## Example 1: "Ship this order to Acme"
```
validate_address({street: "123 Main St", city: "Nairobi", country: "KE"}) → valid ✅
get_rates(from: "warehouse_nbo", to: address, weight: 2.5) → [{carrier: "Sendy", cost: 500, days: 1}, {carrier: "DHL", cost: 2500, days: 2}]
```
Response: "Rates for Nairobi delivery:\n- Sendy: KES 500 (1 day) ← recommended\n- DHL: KES 2,500 (2 days)\nBook Sendy?"

## Example 2: "Where's package 1Z999?"
```
track_shipment(tracking: "1Z999...") → {status: "in_transit", location: "Jomo Kenyatta Airport", last_update: "2h ago"}
get_eta(tracking: "1Z999...") → {estimated: "tomorrow by 5 PM"}
```
Response: "📦 In transit — currently at Jomo Kenyatta Airport (2h ago). ETA: tomorrow by 5 PM."

## Example 3: "Optimize delivery route for 5 stops"
```
optimize_route(stops: ["addr_1", "addr_2", "addr_3", "addr_4", "addr_5"])
→ {optimal_order: [3, 1, 5, 2, 4], total_distance: "45 km", total_time: "1h 20m"}
```
Response: "Optimal route: Stop 3 → 1 → 5 → 2 → 4. Total: 45 km, ~1h 20m."
