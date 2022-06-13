def read_file_content(filename):
    with open(filename) as f:
        content = f.readlines()
        contents=content.copy()
        f.close()
        return contents


print(read_file_content("story.txt"))