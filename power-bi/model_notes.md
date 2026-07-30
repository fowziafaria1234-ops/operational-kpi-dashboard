# Power BI model notes

Recommended star schema:

- `fact_operations`: transactional measures and foreign keys
- `dim_date`: year, month, month name and date key
- `dim_site`: site key and name
- `dim_product`: product key and product-line name

Relationships should be one-to-many from each dimension into the fact table, with single-direction filtering. Mark `dim_date[date]` as the date table.
