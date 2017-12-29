from M2Crypto import BIO, RSA;

message = str(message );
varkey = open(pub_key).read();
# demonstrate how to load key from a string
bio = BIO.MemoryBuffer(varkey);
rsa = RSA.load_pub_key_bio(bio);
# encrypt, IMPORTANT: read about padding modes (RSA.pkcs1_padding)
msgEncrypted = rsa.public_encrypt(message, RSA.pkcs1_padding);

del rsa, bio;