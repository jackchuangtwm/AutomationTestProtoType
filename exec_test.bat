del /S /Q reports\*
.\venv\Scripts\python.exe -m pytest -p no:faulthandler -k "test" --tb=long