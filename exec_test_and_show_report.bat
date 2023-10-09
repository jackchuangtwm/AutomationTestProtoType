del /S /Q results\*
.\venv\Scripts\python.exe -m pytest --alluredir=./results -n 2 --reruns 3 -p no:faulthandler -k "test" --tb=long
.\allure-2.24.1\bin\allure.bat serve results