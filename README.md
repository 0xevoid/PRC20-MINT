# PRC20-MINT
# polsMint
Skrip mint otomatis PRC-20 POLS DLL
Skrip ini juga kompatibel dengan rantai EVM lainnya dan memerlukan 3 modifikasi kode.

 - Ubah alamat rpc: Temukan `rpc_url = "https://1rpc.io/matic"` di kode, buka chainlist.org untuk melihat node rpc yang tersedia untuk penggantian
 - Ubah chainId: Temukan `'chainId': 137` dalam kode, periksa chainId dari rantai yang sesuai menurut chainlist.org dan gantikan
 - Modifikasi data transaksi: Cari `'data' pada kode: '0x646174613a2c7b2270223a227072632d3230222c226f70223a226d696e74222c227469636b223a22706f6c73222c22616d74223 a22313030303030303030227d'', gunakan utf8-hex.py untuk mengonversi string mint dan menggantinya

## Merender
![gambar](https://github.com/0xevoid/inery-3---/blob/main/photo_2023-11-20_16-09-33.jpg)

## Tergantung pada lingkungan
- Lingkungan Python3
- Perintah Git
## Petunjuk penggunaan (versi baru)

### 1. Unduh kode sumber proyek
```
git clone https://github.com/0xevoid/PRC20-MINT.git
```
### 2. Membuat lingkungan virtual Python (langkah opsional)

```
cd PRC20-MINT
python -m venv venv
source venv/bin/activate
```
### 3. Instal dependensi

```
pip instal web3==6.11.3
pip instal python-dotenv==1.0.0
```
### 4. Tulis alamat dan kunci pribadi di file .env

### 5. Jalankan skripnya

```
python pols.py
```
