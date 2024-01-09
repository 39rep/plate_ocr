import easyocr


reader = easyocr.Reader(["en"])
for i in range(1, 25):
    result = reader.readtext(f"/home/god/mp/univ/plate_ocr/yellows/output/number{str(i).zfill(3)}.jpg")
    if result:
        number = result[-1][1:]
    else:
        number = "-----None"
    print(f"plate{str(i)}:\n{number}")

[
    (
        [
            [54, 0], [206, 0], [206, 46], [54, 46]
        ], 
        'Lo ', 
        0.08661511767775976
    ), 
    (
        [
            [92, 42], [238, 42], [238, 118], [92, 118]
        ], 
        '4 88', 
        0.9120393395423889
    )
]