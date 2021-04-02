import os

def main():
    i = 0
    path = "/home/abdulrahman/PycharmProjects/RenamingBulkFiles/Images/"
    for filename in os.listdir(path):
        my_destination = "Image_" + str(i) + ".jpg"
        my_source = path + filename
        my_destination = path + my_destination
        os.rename(my_source, my_destination)
        i += 1

if __name__ == '__main__':
    main()

