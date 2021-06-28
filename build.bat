@echo OFF
python setup.py bdist_wheel --plat-name win32
python setup.py bdist_wheel --plat-name win_amd64
pause