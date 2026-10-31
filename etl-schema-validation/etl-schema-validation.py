def validate_records(records: list, schema: list) -> list:
    results = []

    for record_idx, record in enumerate(records):
        errors = []

        for rule in schema:
            column = rule["column"]
            expected_type = rule["type"]
            nullable = rule["nullable"]

            # Missing check
            if column not in record:
                errors.append(f"{column}: missing")
                continue

            value = record[column]

            # Null check
            if value is None:
                if not nullable:
                    errors.append(f"{column}: null")
                continue

            # Type check
            valid_type = True

            if expected_type == "int":
                valid_type = isinstance(value, int) and not isinstance(value, bool)

            elif expected_type == "float":
                valid_type = (
                    (isinstance(value, (int, float)))
                    and not isinstance(value, bool)
                )

            elif expected_type == "str":
                valid_type = isinstance(value, str)

            if not valid_type:
                errors.append(
                    f"{column}: expected {expected_type}, got {type(value).__name__}"
                )
                continue

            # Range check (only after successful numeric type validation)
            if expected_type in ("int", "float"):
                if "min" in rule and value < rule["min"]:
                    errors.append(f"{column}: out of range")
                    continue

                if "max" in rule and value > rule["max"]:
                    errors.append(f"{column}: out of range")
                    continue

        results.append({
            "record_index": record_idx,
            "is_valid": len(errors) == 0,
            "errors": errors
        })

    return results