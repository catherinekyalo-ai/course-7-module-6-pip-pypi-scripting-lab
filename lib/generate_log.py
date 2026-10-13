from datetime import datetime


def generate_log(data):
    """Write each entry in `data` to a dated log file and return the file name."""
    if not isinstance(data, list):
        raise ValueError("Log data must be a list.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    generate_log(["User logged in", "User updated profile", "Report exported"])
