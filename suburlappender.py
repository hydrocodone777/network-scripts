stored_text = "http://chal.bearcatctf.io:48605"
file_path = "robots.txt"
with open(file_path, 'r') as file:
    for line in file:
        line = line.replace("Allow: ", "").replace("Disallow: ", "")
        line = line.strip()
        combined_text = f'"{stored_text}{line}",'
        print(combined_text)
