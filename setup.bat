pip uninstall mathools
del /S dist\* --force
pipreqs mathools --force --mode gt
python setup.py bdist_wheel
pip install dist\mathools-0.1.0-py3-none-any.whl
pip show mathools