let
    Source = Csv.Document(File.Contents("operations_raw.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(PromotedHeaders,{{"date", type date},{"units_processed", Int64.Type},{"target_units", Int64.Type},{"defects", Int64.Type},{"downtime_minutes", Int64.Type},{"labour_hours", type number},{"cost_gbp", Currency.Type},{"revenue_gbp", Currency.Type}}),
    RemovedDuplicates = Table.Distinct(Typed, {"transaction_id"}),
    FilledSite = Table.ReplaceValue(RemovedDuplicates,null,"Unknown",Replacer.ReplaceValue,{"site"}),
    AddedVariance = Table.AddColumn(FilledSite,"variance_units",each [units_processed]-[target_units],Int64.Type),
    AddedDefectRate = Table.AddColumn(AddedVariance,"defect_rate",each [defects]/[units_processed],Percentage.Type)
in
    AddedDefectRate
