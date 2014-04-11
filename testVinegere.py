def main():

    newKey = ""
    message = "THISPROGRAMWILLBEGREAT"
    key = "PYTHON"

    multiplier = int(len(message) / len(key))
    remainder = len(message) % len(key)

    newKey += key * multiplier + key[:remainder]
    print(newKey)
main()
