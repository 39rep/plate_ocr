import easyocr


reader = easyocr.Reader(["ja", "en"])
result = reader.readtext("result.jpg")

print(result)