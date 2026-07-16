# CXC
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-v1.2.25.10-orange)

**📔INDONESIA**

hallo saya xyrion, saya membagikan alat yang mungkin akan membantu anda dalam hal seperti, download music mp3, play music, chat dengan ai menggunakan api key anda sendiri, anda bisa mengatur semua config nya di dalam file yang bernama config.py, yang berlokasi, di folder .config/ai di home komputer anda.

**📘ENGLISH**

Hello, I'm xyrion, I'm sharing a tool that might help you in things like, downloading mp3 music, plays music, chatting with AI using your own API key, you can set all the configurations in a file called config.py, which is located in the .config/ai folder on your computer's home page. 

# **🔑GET API key**

**📔INDONESIA**

Pada bagian ai anda memerlukan api key gemini ai, karena pada dasar nya alat yang saya buat berbasis gemini ai, kalau anda hanya memerlukan alat untuk mendownload music nya saja anda tidak perlu api key ini. Untuk mendapat kan api key gemini, anda bisa membuka

<https://aistudio.google.com/>

**📘ENGLISH**

For the AI section, you'll need the Gemini AI API key, as the tool I created is essentially based on Gemini AI. If you only need the tool to download music, you don't need this API key. To get the Gemini API key, You can get your Gemini API KEY at

<https://aistudio.google.com/>

# **📖COMMAND**

**📔INDONESIA**

- help Menampilkan informasi lanjut tentang command yg tersedia
- search [query] Mencari Informasi Music
- download [query] Mendownload Music 
- play [query] Memutar Music menggunakan mpv
- time Menampilkan Tanggal, Bulan, Tahun, Hari dan Waktu
- chat Membuka menu Chat dengan Ai

**📘ENGLISH**

- help displays further information about available commands 
- search [query] Searching for Music Information 
- download [query] Download Music 
- play [query] Plays Music using mpv 
- time Displays Date, Month, Year, Day and Time 
- chat Open the Chat menu with Ai


# **Requirements**

- yt-dlp
- requests
- textual
- mpv

# Features

- 🎵 Search music
- ⬇️ Download MP3
- ▶️ Play music with MPV
- 🤖 Chat with Gemini AI
- 🕒 Show date & time

# Installation

```bash
pip install cxc
```

# Operate
- cxc help < Display the help menu 
- cxc search < Searching for music using yt-dlp
- cxc download < Download music according to the query you provide
- cxc play < Play music according to the query you provide 
- cxc chat < Open the chat menu with AI 
- cxc list < Displays a list of available music 

# Example
cxc download "tabola bale"

# Setting your AI Configuration
```bash
nano ~/.config/cxc/config.py
```
