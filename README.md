# Logistics & Shipping Skill

> Multi-carrier shipping for AI agents — create shipments, compare rates, track packages, optimize routes, validate addresses, and generate labels across ShipEngine, Shippo, Sendy (Africa), and Google Maps.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--logistics-green)](https://github.com/zavora-ai/mcp-logistics)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

This skill orchestrates 16 logistics tools into **cost-optimized shipping workflows** — ensuring addresses are validated before shipping, rates are compared before booking, and every package is tracked to delivery.

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Ship Package | 5 | Validate → rates → compare → book → label |
| Track | 2 | Current status + ETA |
| Rate Comparison | 2-3 | Cheapest vs fastest options |
| Route Optimization | 1-2 | Multi-stop delivery planning |
| Address Validation | 1 | Prevent failed deliveries |

### Without this skill:
- Packages shipped to unvalidated addresses (failed deliveries)
- Most expensive carrier selected by default
- No tracking visibility after shipment
- Multi-stop routes unoptimized (wasted time/fuel)

### With this skill:
- Address validated before every shipment
- Rates compared automatically (cheapest vs fastest presented)
- Real-time tracking with ETA for every package
- Multi-stop routes optimized for distance/time

## Installation

```bash
git clone https://github.com/zavora-ai/skill-logistics-shipping.git \
  ~/.skills/skills/logistics-shipping
```

## Requirements

**Required:** `mcp-logistics` (16 tools — ShipEngine, Shippo, Sendy, Google Maps)

**Cross-MCP:**
- `mcp-erp` — order fulfillment triggers shipping
- `mcp-email` — send tracking info to customers
- `mcp-notifications` — delivery alerts
- `mcp-slack` — shipping exception alerts

## Multi-Region Coverage

| Backend | Region | Capabilities |
|---------|--------|-------------|
| ShipEngine | US, Global | Rates, labels, tracking |
| Shippo | US, Global | Rates, labels, tracking |
| Sendy | Kenya, Nigeria, Ghana | Last-mile delivery |
| Google Maps | Global | Route optimization, ETA, distance |

## Folder Structure

```
logistics-shipping/
├── SKILL.md                       # Decision tree + 5 workflows + validation rules
├── scripts/
│   └── validate_address.py        # Address format validation (US/CA postal codes)
├── references/
│   ├── tool-sequences.md          # 16 tools with exact call patterns
│   ├── cross-mcp-workflows.md     # Logistics + ERP + Email + Notifications
│   └── examples.md                # Ship, track, optimize route
├── README.md
└── LICENSE
```

## Example

**User:** "Ship this order to Nairobi"

**Agent behavior:**
1. Validates address format
2. Gets rates from all carriers (Sendy, DHL)
3. Presents options: Sendy KES 500 (1 day) vs DHL KES 2,500 (2 days)
4. On selection: books rate + generates label

**Result:**
```
✅ Shipment booked via Sendy
Tracking: SNY-12345
ETA: Tomorrow by 5 PM
Label generated: [download link]
```

## Success Criteria

| Metric | Target |
|--------|--------|
| Address validation | 100% validated before shipping |
| Cost optimization | Always compare rates before booking |
| Tracking | Real-time status on every shipment |
| Failed deliveries | 0 due to bad addresses |

## Scripts

### `validate_address.py`
```bash
python scripts/validate_address.py '{"street": "123 Main St", "city": "Nairobi", "country": "KE"}'
# → {"valid": true, "errors": [], "warnings": []}
```

## MCP Server Compatibility

| Category | Tools |
|----------|-------|
| Shipments | create, list, get, cancel |
| Rates | get_rates, compare_rates, list_carriers, book_rate |
| Tracking | track_shipment, get_tracking_events |
| Labels | generate_label, get_label |
| Routing | validate_address, optimize_route, get_eta, get_distance |

## Related Skills

- [skill-erp-operations](https://github.com/zavora-ai/skill-erp-operations) — Order fulfillment
- [skill-email-management](https://github.com/zavora-ai/skill-email-management) — Shipping confirmations

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0

---

Part of the [ADK-Rust Enterprise](https://enterprise.adk-rust.com) skills ecosystem. Built with ❤️ by [Zavora AI](https://zavora.ai)
