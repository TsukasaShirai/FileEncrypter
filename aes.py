
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random

class FileEncrypter:
	def encryptFile(self, inputFile, outputFile, password):
		with open(inputFile, "rb") as target:
			contents = target.read()
		data = self.encrypt(contents, password)
		with open(outputFile, "wb") as result:
			result.write(data)

	def decryptFile(self, inputFile, outputFile, password):
		with open(inputFile, "rb") as target:
			contents = target.read()
		data = self.decrypt(contents, password)
		with open(outputFile, "wb") as result:
			result.write(data)

	def create_aes(self, password, iv):
		sha = SHA256.new()
		sha.update(password.encode())
		key = sha.digest()
		return AES.new(key, AES.MODE_CFB, iv)

	def encrypt(self, data, password):
		iv = Random.new().read(AES.block_size)
		return iv + self.create_aes(password, iv).encrypt(data)

	def decrypt(self, data, password):
		iv, cipher = data[:AES.block_size], data[AES.block_size:]
		return self.create_aes(password, iv).decrypt(cipher)