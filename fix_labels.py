import os

folders = [
r"C:\Users\Shasmeen Begum\yolov5\weed_dataset\labels\train",
r"C:\Users\Shasmeen Begum\yolov5\weed_dataset\labels\val"
]

for folder in folders:
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            path = os.path.join(folder, file)

            with open(path, "r") as f:
                lines = f.readlines()

            new_lines = []
            for line in lines:
                parts = line.split()
                if len(parts) > 0:
                    parts[0] = "0"
                    new_lines.append(" ".join(parts) + "\n")

            with open(path, "w") as f:
                f.writelines(new_lines)

print("All labels fixed")