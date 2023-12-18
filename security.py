import os
from google.colab import runtime

def secure_notebook():
  """Secures the current Colab notebook by making it read-only."""

  notebook = runtime.get_notebook()

  notebook.set_readonly(True)

secure_notebook()
