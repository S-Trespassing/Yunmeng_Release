import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# 根据图片提取的配置信息
KEY = b"K7mP9zL4xQ2vW5cY"
IV = b"N3bA6vC8xZ1mK9pL"


def encrypt_data(plaintext):
    """
    使用 AES-128-CBC 和 PKCS7 填充加密字符串
    """
    # 1. 创建 AES CBC 模式的 Cipher 对象
    cipher = AES.new(KEY, AES.MODE_CBC, IV)

    # 2. 对明文进行 PKCS7 填充 (pad 函数默认使用 PKCS7)
    # AES 的 block size 固定为 16 字节
    padded_data = pad(plaintext.encode('utf-8'), AES.block_size)

    # 3. 加密数据
    encrypted_bytes = cipher.encrypt(padded_data)

    # 4. 将加密后的二进制数据转换为 Base64 字符串，方便写入文本文件
    encrypted_base64 = base64.b64encode(encrypted_bytes).decode('utf-8')

    return encrypted_base64


def main():
    # 从外界读取用户输入
    user_input = input("请输入需要加密的内容: ")

    if not user_input:
        print("输入为空，已取消操作。")
        return

    try:
        # 执行加密
        encrypted_result = encrypt_data(user_input)

        # 将结果覆盖写入同文件夹的 config.txt ("w" 模式代表覆盖写入)
        with open("config.txt", "w", encoding="utf-8") as file:
            file.write(encrypted_result)

        print("\n✅ 加密成功！")
        print(f"加密后的结果为: {encrypted_result}")
        print("该结果已成功覆盖写入到当前目录的 config.txt 文件中。")

    except Exception as e:
        print(f"\n❌ 加密过程中发生错误: {e}")


if __name__ == "__main__":
    main()