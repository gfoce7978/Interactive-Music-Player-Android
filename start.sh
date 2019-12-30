export PYTHONWARNINGS="ignore"
script_output=$(python -W ignore emotions.py --mode Test.jpg 2>&1)
echo $script_output
return $script_output
