pip uninstall math_extended
pipreqs ./mathext --force --mode gt
python .\setup.py bdist_wheel
pip install dist\math_extended-0.1-py3-none-any.whl
pip show math_extended