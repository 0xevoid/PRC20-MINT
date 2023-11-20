data = 'data:,{"p":"prc-20","op":"mint","tick":"pols","amt":"100000000"}'
# Konversikan string ke byte yang dikodekan UTF-8
utf8_bytes = data.encode('utf-8')
# Ubah byte menjadi representasi string heksadesimal
hex_str = utf8_bytes.hex()
print("0x"+hex_str)
