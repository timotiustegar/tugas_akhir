import os
import schedule
import time
import threading

def hapus_semua_file():
    folder_path = 'dataset/'

    # Ambil daftar file dalam folder
    file_list = os.listdir(folder_path)

    # Hapus setiap file dalam folder
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print("Semua file telah dihapus.")

def jadwal_hapus_file():
    # Jadwalkan penghapusan semua file setiap pukul 00.00
    schedule.every().day.at("00:00").do(hapus_semua_file)

    # Jalankan scheduler sekali
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start thread untuk menjalankan scheduler
thread = threading.Thread(target=jadwal_hapus_file)
thread.start()

import streamlit as st
import pandas as pd
uploaded_file = st.file_uploader("Upload file")
df = pd.DataFrame()
# Simpan file
if uploaded_file is not None:
    path = "dataset/"
    with open(path + uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    temp = pd.read_csv(path+uploaded_file.name)
    df=temp.copy()
st.dataframe(df)
