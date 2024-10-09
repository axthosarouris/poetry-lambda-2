rm -rf artifact.zip
poetry build
poetry run pip install --upgrade -t package dist/*.whl
(cd package && zip  -r ../artifact.zip . -x 'package/*.pyc')
rm -rf package
poetry run sam build -t template.yaml
