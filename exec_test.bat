del /S /Q results\*
python -m venv venv
.\venv\Scripts\pip.exe install -r requirements.txt --target=.\venv\Lib\site-packages --upgrade
.\venv\Scripts\python.exe -m pytest -n 2  --alluredir=./results --reruns 3 -p no:faulthandler -k "test" --tb=long
