import hashlib

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
    "5f53734c5153ec3dd61e2a732a2ff03f",
    "4fdf58bbef65184e13094e09e43135ae",
    "76a8b4d77a0aa32453fb51cab9bbf92e",
    "9d2dfb7c0d765b18ec67f6eb2b784ca3",
    "0973e2226ff43e68cf9b1e3b4cb25dd7",      # Malware hash database: https://raw.githubusercontent.com/aaryanrlondhe/Malware-Hash-Database/refs/heads/main/MD5/md5_hashes_1.txt
    "db063c7f3eeed0ac66c3c42fd3797f59",
    "96c45dfdbbe0457a2792e73265c2a5bd",
    "8e4c0eeb469f011e6aea3dbd07106515",
    "adc9bff956052e496d06bb9d848ffb32",
    "d436dc7faa63db35b10524ac82ab7631",
    "777396c8d1529dad186a2e954ab9a40c",
    "113835dd31fad6c8639724879be38053",
    "1272bf402ae8ccbb3cf205ff7a41c254"
]

file_path = input("Enter filename to scan: ")
file_hash = compute_md5(file_path)

if file_hash in malware_hashes:
    print(f"WARNING!!! {file_path} IS INFECTED")
else:
    print("File not infected!")
