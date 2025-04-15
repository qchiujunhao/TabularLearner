## Get started
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python tools/main.py
```
if you are using macOS you might encounter the following error
```
/System/Volumes/Preboot/Cryptexes/OS/opt/local/lib/libomp/libomp.dylib' (no such file)`.
```
if so, you can fix it by installing `libomp` via Homebrew
```bash
brew install libomp
```