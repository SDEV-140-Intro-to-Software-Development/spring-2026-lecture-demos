import os
import struct

def write_save_data(data):
    path = os.path.join("2026-2-17-lecture-11","binary-example","save-data.dat")
    f = open(path, "wb")
    f.write(b"asd")
    f.write(data["currency"].to_bytes(1))
    f.write(data["health"].to_bytes(1))
    f.write(data["x"].to_bytes(1))
    f.write(data["y"].to_bytes(1))
    f.close()

def read_save_data():
    path = os.path.join("2026-2-17-lecture-11","binary-example","save-data.dat")
    f = open(path, "rb")
    content = f.read()
    f.close()
    raw_data = struct.unpack(">sssbbbb", content)
    data = {
        "currency": raw_data[3],
        "health": raw_data[4],
        "x": raw_data[5],
        "y": raw_data[6]
    }
    return data

data = {
    "currency": 10,
    "health": 100,
    "x": 15,
    "y": 10
}

write_save_data(data)
print(read_save_data())