from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def generate_key_pair():
    # 生成私鑰
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    
    # 從私鑰獲取公鑰
    public_key = private_key.public_key()
    
    # 將私鑰序列化為 PEM 格式
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    # 將公鑰序列化為 PEM 格式
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    # 將結果寫入文件
    with open('private_key.pem', 'wb') as f:
        f.write(private_pem)
    
    with open('public_key.pem', 'wb') as f:
        f.write(public_pem)

if __name__ == '__main__':
    generate_key_pair()
