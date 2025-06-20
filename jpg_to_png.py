from PIL import Image

for i in range(361, 401):
    img = Image.open(f"datasets/facades/images/testing/{i}_A.jpg")
    img.save(f"datasets/facades/images/testing/{i}_A.png", "PNG")
