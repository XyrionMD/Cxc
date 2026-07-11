#<==> TERMUX <==> For Termux, you can remove the hash mark under this text, then save it again and run it.
# |
# V
#pkg update -y && pkg install mpv figlet
echo "Succesly Install Library"
sleep 1
echo "Installing ai..."
mkdir -p build && cp src/Ai/ai build && chmod +x build/ai
mkdir -p $HOME/.config/ai && cp src/Ai/colors.py $HOME/.config/ai/

cp src/Ai/chat.py $HOME/.config/ai && cp src/Ai/config.py $HOME/.config/ai
