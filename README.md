# 數位簽署與驗證的步驟

## app1.py 為主應用程訊
1. 啟動時，先計算自己 (app1.py) 的 SHA256 哈希值
2. 讀取 hash_signed, 並利用 public_key 解密還原簽署時的哈希值
3. 驗證上述兩個哈希值是否相等

## cal_n_sign.py 的功能
1. 計算 app1.py 的 SHA256 哈希值，保存為 hash.txt
2. 使用 private_key 簽署 (加密)，保存為 hash_signed

## 部署
1. app1.py, hash_signed 保存在 eMMC 上
2. public_key 客戶燒到 eMMC 特殊位址
3. cal_n_sign.py, hash.txt 與 private_key，客戶自己要收好
