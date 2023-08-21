git clone https://github.com/nixtla/transfer-learning-time-series
cp transfer-learning-time-series/datasets/electricity-short.csv ./electricity.csv
pip install -r requirements.txt && python -m src.filter_dataset && tmux
