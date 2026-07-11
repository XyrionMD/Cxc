# **📔INDONESIA**

hallo saya xyrion, saya membagikan alat yang mungkin akan membantu anda dalam hal seperti, download music mp3, play music, chat dengan ai menggunakan api key anda sendiri, anda bisa mengatur semua config nya di dalam file yang bernama config.py, yang berlokasi, di folder .config/ai di home komputer anda.

# **📘ENGLISH**

Hello, I'm xyrion, I'm sharing a tool that might help you in things like, downloading mp3 music, playing music, chatting with AI using your own API key, you can set all the configurations in a file called config.py, which is located in the .config/ai folder on your computer's home page. 

# **🔑GET API key**

**📔INDONESIA**

Pada bagian ai anda memerlukan api key gemini ai, karena pada dasar nya alat yang saya buat berbasis gemini ai, kalau anda hanya memerlukan alat untuk mendownload music nya saja anda tidak perlu api key ini. Untuk mendapat kan api key gemini, anda bisa menonton video tutorial di youtube.

**📘ENGLISH**

For the AI section, you'll need the Gemini AI API key, as the tool I created is essentially based on Gemini AI. If you only need the tool to download music, you don't need this API key. To get the Gemini API key, you can watch the tutorial video on YouTube. 

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
- play [query] Playing Music using mpv 
- time Displays Date, Month, Year, Day and Time 
- chat Open the Chat menu with Ai


# **requirements**

- yt-dlp
- requests
- lolcat
- figlet
- mpv

**Step 1**

```bash
git clone https://github.com/XyrionMD/AiTools.git
```

**Step 2**
```bash
cd AiTools
```
**Step 3**
```bash
pip install -r requirements.txt
```
**Step 4**
install mpv dan figlet melalui packages manager distro anda/install mpv and figlet via your distro's packages manager 

**Step 5**
```bash
bash install.sh
```
# Operate
**The main file, named ai, will be automatically created in the build folder. You can run it with**
```bash
python3 ai
```

# Setting your AI Configuration
```bash
nano ~/.config/ai/config.py
```
