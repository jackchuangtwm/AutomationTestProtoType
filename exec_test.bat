del /S /Q results\*
.\venv\Scripts\python.exe -m pytest -n 2  --alluredir=./results --reruns 3 -p no:faulthandler -k "test" --tb=long
