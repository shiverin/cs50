x=input("file").strip().lower()
z="image"
for y in ("gif","jpg","jpeg","png","pdf","zip","txt"):
    if x.endswith(f".{y}"):
        if y=="jpg":
            y="jpeg"
        elif y=="zip" or y=="pdf":
            z="application"
        elif y=="txt":
            z="text"
            y="plain"
        print(f"{z}/{y}")
        break

else:
    print("application/octet-stream")
