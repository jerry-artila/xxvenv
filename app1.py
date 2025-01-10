import hashlib
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def calculate_file_hash():
    """計算當前文件的 SHA256 雜湊值"""
    with open(__file__, 'r', encoding='utf-8') as f:
        content = f.read()
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def load_public_key():
    """載入公鑰"""
    with open('public_key.pem', 'rb') as key_file:
        return serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

def verify_signature(public_key, signature, hash_content):
    """驗證數位簽名"""
    try:
        public_key.verify(
            signature,
            hash_content,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"數位簽名驗證失敗: {str(e)}")
        return False

def app1():
    print("Hello, World!")

if __name__ == '__main__':
    # 計算並顯示當前文件雜湊值
    file_hash = calculate_file_hash()
    print(f"當前文件的 SHA256 雜湊值: {file_hash}")

    # 載入必要資料
    public_key = load_public_key()
    with open('hash_signed', 'rb') as f:
        signature = f.read()

    # 驗證簽名
    if verify_signature(public_key, signature, file_hash.encode('utf-8')):
        print("數位簽名驗證成功!")
        app1()
