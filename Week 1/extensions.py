filename = input("File name:").lower().strip().split(".")

image = ["gif","png"]
text = ["txt"]
application = ["pdf","zip"]

if  filename[-1] in application:
    print(f"application/{filename[-1]}")

elif filename[-1] == "jpg" or filename[-1] == "jpeg":
    print(f"image/jpeg")

elif filename[-1] in image:
    print(f"image/{filename[-1]}")

elif filename[-1] in text:
    print(f"text/plain")

else:
    print("application/octet-stream")
