import os
from google.colab import notebook

def secure_notebook():
  """Secures the current Colab notebook by making it read-only."""

  notebook.get_notebook()

  notebook.set_readonly(True)

secure_notebook()
