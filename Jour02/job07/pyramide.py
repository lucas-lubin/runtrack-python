def pyramide(string, height):
    for i in range(1, height + 1):
        spaces = " " * (i - 1)
        layer = string[:i * 2 - 1][::-1]
        print(spaces + layer.center(height * 2 - 1))

base_string = "abcdefghijklmnopqrstuvwxyz"
pyramide_height = 10
pyramide(base_string, pyramide_height)