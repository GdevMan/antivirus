import hashlib
import os
def compute_md5(path: str) -> str:
    md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            md5.update(chunk)
    return md5.hexdigest()

malware_hashes = [
    "64ba34ffc6f57a759429ab3d2885efa5",
    "111bd3cf0217dda4cbde6c06cdaa10d8",
    "d6357a81f58aef5af24d98cd0f454709",
    "8b62b90b65e21566b2a6267ecdc8357c",
    "655d3d7d35fff093109abdae45d85bdb",
    "ec882e9e6b1c6508042a72d47763ea01",
    "6174fe1f2be2da7c4ba1589afeda0eae",
    "1bfc70047c0bea43c64172be8e4ac30c",
    "e561309860dfb3cc923295a0b41b094a",
    "959cab796f6eeb75343fe4c381ccc86e",
    "718c8b9ba838a22b1054c3108d8b7df5",
    "3a831bdaefdeeb1ddadbc23847bab137",
    "f0c1583cb78262833587ed0c5096fcd6",
    "794ff4e6293c6b1cc90dca6d03bc1706",
    "ffb58908322fccc5932ebfe0f4f4205b",
    "22875e4ab1bd561974b973882990e203",
    "4eefa3b17a7c03c6048b7a5eaf2507e7",
    "92d8a61ed6cfa03b50d284115e6b62b8",
    "ccf1c8baef1ac381c1655d9fcdd6a6e8",                         # Malware hash database: https://raw.githubusercontent.com/aaryanrlondhe/Malware-Hash-Database/refs/heads/main/MD5/md5_hashes_1.txt
    "bed16f163a1feddfd5bbfebc5e652d32",
    "e7efeb84cefe05c346f93d617c6ae2b7",
    "5f53734c5153ec3dd61e2a732a2ff03f",
    "4fdf58bbef65184e13094e09e43135ae",
    "76a8b4d77a0aa32453fb51cab9bbf92e",
    "9d2dfb7c0d765b18ec67f6eb2b784ca3",
    "0973e2226ff43e68cf9b1e3b4cb25dd7",
    "db063c7f3eeed0ac66c3c42fd3797f59",
    "96c45dfdbbe0457a2792e73265c2a5bd",
    "8e4c0eeb469f011e6aea3dbd07106515",
    "adc9bff956052e496d06bb9d848ffb32",
    "d436dc7faa63db35b10524ac82ab7631",
    "777396c8d1529dad186a2e954ab9a40c",
    "113835dd31fad6c8639724879be38053",
    "1272bf402ae8ccbb3cf205ff7a41c254"
]
def main():                                                     # Dashboard
    file_path = input("Enter filename to scan: ")
    file_hash = compute_md5(file_path)
    scan()
def scan():                                                     # Scanning part
    if file_hash in malware_hashes:
        print(f"WARNING!!! {file_path} IS INFECTED")
        ask = input("Do you want to delete it: (Y/N)")          # confirmation
        if ask == "Y" or "Yes" or "yes" or "y":                 # confirmation
            os.remove(file_path)
            if FileNotFoundError:                               # Error check
                print('ERROR : File Not Found')
        elif ask == "N" or "No" or "no" or "n":                 # confirmation
            print('Ok.')
    else:
        print("File not infected!")
