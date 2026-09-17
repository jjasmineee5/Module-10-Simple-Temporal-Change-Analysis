def calculate_vegetation_change(before_coverage, after_coverage):
    change = after_coverage - before_coverage

    return {
        "before": before_coverage,
        "after": after_coverage,
        "change": change
    }


if __name__ == "__main__":
    # Dummy data untuk testing
    before_coverage = 60.0
    after_coverage = 72.0

    result = calculate_vegetation_change(
        before_coverage,
        after_coverage
    )

    print("Before :", result["before"], "%")
    print("After  :", result["after"], "%")
    print("Change :", result["change"], "percentage points")