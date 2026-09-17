def manage_multi_date_images(images):
    grouped_images = {}

    for image in images:
        date = image["acquisition_date"]

        if date not in grouped_images:
            grouped_images[date] = []

        grouped_images[date].append(image["image_path"])

    return grouped_images

images = [
    {
        "image_path": "data/image_01.tif",
        "acquisition_date": "2026-01-10"
    },
    {
        "image_path": "data/image_02.tif",
        "acquisition_date": "2026-02-10"
    },
    {
        "image_path": "data/image_03.tif",
        "acquisition_date": "2026-02-10"
    }
]

result = manage_multi_date_images(images)

print(result)