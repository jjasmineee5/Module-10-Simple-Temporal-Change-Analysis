def compare_before_after(before_image, after_image):
    return {
        "before": before_image,
        "after": after_image
    }


# Test
before = {
    "image_path": "data/image_01.tif",
    "acquisition_date": "2026-01-10"
}

after = {
    "image_path": "data/image_02.tif",
    "acquisition_date": "2026-02-10"
}

result = compare_before_after(before, after)

print("Before:", result["before"])
print("After:", result["after"])
