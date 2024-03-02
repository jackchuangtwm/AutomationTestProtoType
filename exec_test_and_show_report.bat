del /S /Q results\*
python -m venv venv
.\venv\Scripts\pip.exe install -r requirements.txt --target=.\venv\Lib\site-packages --upgrade
.\venv\Scripts\python.exe -m pytest --alluredir=./results -n 2 --reruns 3 -p no:faulthandler -k "test" --tb=long
.\allure-2.24.1\bin\allure.bat serve results