import base64
def key_scheduling(key):
    sched = [i for i in range(0, 256)]
    
    i = 0
    for j in range(0, 256):
        i = (i + sched[j] + key[j % len(key)]) % 256
        
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp
        
    return sched
def stream_generation(sched):
    stream = []
    i = 0
    j = 0
    while True:
        i = (1 + i) % 256
        j = (sched[i] + j) % 256
        
        tmp = sched[j]
        sched[j] = sched[i]
        sched[i] = tmp
        
        yield sched[(sched[i] + sched[j]) % 256]        
def decrypt(ciphertext, key):
    ciphertext = ciphertext.split('0X')[1:]
    ciphertext = [int('0x' + c.lower(), 0) for c in ciphertext]
    key = [ord(char) for char in key]
    sched = key_scheduling(key)
    key_stream = stream_generation(sched)
    plaintext = ''
    for char in ciphertext:
        dec = str(chr(char ^ next(key_stream)))
        plaintext += dec
    return plaintext
if __name__ == '__main__':
    try:
        with open("encryptedcode.txt", "r")  as f:
            ciphertext = f.read()
        ciphertext = ciphertext
        key = input('Enter your secret key: ')
        result = decrypt(ciphertext, key)
        result = base64.b64decode(str(result))
        with open("runme.py", "w") as d:
            d.write(str(result.decode("utf-8")))
        print("Decrypted Successfully!!!!!! yay your so close")
    except:
        print("Make Sure You Have The File encryptedcode.txt and in the same directory")