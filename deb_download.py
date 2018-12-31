from urllib.request import urlopen
import os

class deb:
    count = 0

    def __init__(self, url, dir):
        dir_list = list(dir)
        if dir_list[len(dir_list)-1] != "/":
            self.dir = dir + "/"
        else:
            self.dir = dir

        if os.path.isdir(dir) != True:
            os.mkdir(dir)
        self.url = url
        deb.count += 1

    def download(self):
        response = urlopen(self.url)

        filename = self.url.split("/")
        filename = filename[len(filename)-1].replace('\n', '')
        self.filename = filename
        print("# Downloading " + filename)
        filepath = self.dir + filename

        download = open(filepath, "wb")
        download.write(response.read())
        download.close()
        print("# Download Complete!\n")

def downloadDebsFromFile(filename, directory):
    with open(filename) as file:
        for line in file:
            debLine = deb(line, directory)
            debLine.download()

downloadDebsFromFile("packages", "tmp")
