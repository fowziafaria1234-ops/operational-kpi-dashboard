# Data dictionary

| Field | Type | Meaning |
|---|---|---|
| transaction_id | text | Unique operational record identifier |
| date | date | Activity date |
| site | category | Operating location |
| department | category | Process area |
| product_line | category | Product family |
| units_processed | integer | Completed units |
| target_units | integer | Planned units |
| defects | integer | Quality defects recorded |
| downtime_minutes | integer | Operational downtime |
| labour_hours | decimal | Labour effort |
| on_time_flag | 0/1 | Whether the record met service criteria |
| cost_gbp / revenue_gbp | currency | Financial inputs |
| variance_units | integer | Units minus target |
| defect_rate | decimal | Defects divided by units |
| gross_margin_gbp | currency | Revenue minus cost |
