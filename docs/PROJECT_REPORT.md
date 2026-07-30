# Operational KPI Dashboard — Project Report

## Business problem

Recurring operational reports were being rebuilt manually. The goal was to create a refreshable reporting model that defined KPIs once, applied documented validation rules and enabled users to explore performance without repeated ad-hoc requests.

## Method

1. Generated a realistic raw extract with duplicates, missing values and malformed dates.
2. Applied Power Query/Python-style cleansing and type conversion.
3. Designed a star schema with date, site and product dimensions.
4. Defined DAX measures for volume, attainment, quality, on-time delivery, downtime and margin.
5. Built an interactive browser dashboard and static visual evidence.

## Demonstration findings

- Overall target attainment: **101.1%**
- Defect rate: **2.07%**
- On-time performance: **74.5%**
- Total gross margin in the demonstration period: **£837,450**
- Best on-time performance: **Unknown**

## Recommendation

Use the dashboard as a weekly control point, investigate departments with elevated downtime, and maintain a formal metric dictionary so operational teams use consistent definitions.
