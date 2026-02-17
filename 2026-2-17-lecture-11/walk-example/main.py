import os

def find_first_file(path):
    for dirname, subdirs, files in os.walk(path):
        if len(files) > 0:
            return os.path.join(dirname, files[0])

def find_all_files_with_extension(path, ext):
    output = []
    # do the loop
        # if file has extension, add to output

    return output


path = os.path.join("2026-2-17-lecture-11", "walk-example" , "logs")
# for dirname, subdirs, files in os.walk(path):
#     print(dirname, subdirs, files)

print(find_first_file(path))