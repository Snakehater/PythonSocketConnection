cd /Applications/Python\ 3.6/
./Install\ Certificates.command
codesign --force --sign "My Signing Identity" /Library/Frameworks/Python.framework/Versions/3.6/Resources/Python.app
python3 Server.py