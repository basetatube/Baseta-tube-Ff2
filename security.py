import os
from google.colab import colab_notebook

def secure_notebook():
    """Secures the current Colab notebook by making it read-only."""
    current_notebook = colab_notebook.get_notebook()
    current_notebook.set_readonly(True)

secure_notebook()
