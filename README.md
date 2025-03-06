# 3spiel

curl -LsSf https://astral.sh/uv/install.sh | sh
uv init
uv run main.py
uv add umap-learn[tbb]
uv add umap-learn[plot]
uv add --dev ipykernel
uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=project
uv run --with jupyter jupyter lab # Not necessary