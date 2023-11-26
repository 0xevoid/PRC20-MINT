from web3 import Web3,Account

#informasi rpc
rpc=''
#Terima alamat
to_address = '0x'
#kunci pribadi Anda sendiri
private_key='d'
lim=1000 #Berapa banyak gambar yang harus saya putar? 5u berarti 1k gambar. Yang terbaik adalah menyiapkan 6u.


#Hubungkan ke simpul rpc
w3 = Web3(Web3.HTTPProvider(rpc))
from_address = Account.from_key(private_key).address
print('koneksi internet：',w3.is_connected())
#Tentukan tautan jaringan
if w3.is_connected() ==True:
    #Dapatkan nonce saat ini
    nonce=w3.eth.get_transaction_count(from_address)
    # Dapatkan harga gas saat ini
    gas_price = w3.eth.gas_price
    # Konversi harga bahan bakar dari Wei ke Gwei
    gas_price_gwei = w3.from_wei(gas_price, 'Gwei')
    data = 'data:,{"a":"NextInscription","p":"oprc-20","op":"mint","tick":"NI","amt":"10000"}'
    print("saat ini nonce:",nonce,"saat ini gas:",gas_price_gwei,'alamat pengirim:',from_address)
    # Kirim transaksi secara batch
    for i in range(lim):
        transaction = {
            'from': from_address,  # from：alamat pengirim
            'to': to_address,  # to：alamat penerima
            'value': w3.to_wei(0, 'ether'),  # value：Jumlah eter yang dikirim (bilangan bulat)。Ini adalah jumlah Ethereum di Wei。1 Eter sama dengan 10^18 Wei。
            'nonce': nonce,  # nonce：Jumlah transaksi alamat pengirim (integer). Ini digunakan untuk memastikan keunikan transaksi.
            'gas': 25000,  # gas：Menentukan kuantitas gas (bilangan bulat) yang akan digunakan untuk transaksi. Gas digunakan untuk melakukan operasi komputasi dan penyimpanan transaksi.
            'gasPrice': gas_price,  # gasPrice：Harga gas (bilangan bulat). Harga satuan gas di Wei digunakan untuk menghitung biaya gas dalam transaksi.
            'data': w3.to_hex(text=data),  # Data khusus untuk ditambahkan ke Data Input
            'chainId': w3.eth.chain_id  # 区identitas blockchain
        }
        # 2.transaksi tanda tangan
        signed = w3.eth.account.sign_transaction(transaction, private_key)
        try:
            # 3.kesepakatan siaran
            tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
            print("Hash:", tx_hash.hex(),'noce:',nonce)
        except Exception as e:
            print('Terjadi kesalahan transaksi',e,'berdagang data：',data)
        nonce+=1
