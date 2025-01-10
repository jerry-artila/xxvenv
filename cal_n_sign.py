import hashlib
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def calculate_file_hash(filename):
    """計算指定檔案的 SHA256 雜湊值"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def save_hash(hash_value, filename='hash.txt'):
    """將雜湊值儲存到檔案"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(hash_value)

def load_private_key(key_file='private_key.pem'):
    """載入私鑰"""
    with open(key_file, 'rb') as f:
        return serialization.load_pem_private_key(
            f.read(),
            password=None,
            backend=default_backend()
        )

def sign_hash(private_key, hash_content):
    """使用私鑰對雜湊值進行簽署"""
    return private_key.sign(
        hash_content,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

def save_signature(signature, filename='hash_signed'):
    """儲存簽署後的內容"""
    with open(filename, 'wb') as f:
        f.write(signature)

def main():
    # 計算 app1.py 的雜湊值
    file_hash = calculate_file_hash('app1.py')
    print(f"app1.py 的 SHA256 雜湊值: {file_hash}")
    
    # 儲存雜湊值
    save_hash(file_hash)
    print("雜湊值已儲存至 hash.txt")
    
    # 載入私鑰並進行簽署
    private_key = load_private_key()
    with open('hash.txt', 'rb') as f:
        hash_content = f.read()
    
    signature = sign_hash(private_key, hash_content)
    
    # 儲存簽署結果
    save_signature(signature)
    print("已簽署的雜湊值已儲存至 hash_signed")

if __name__ == '__main__':
    main()
