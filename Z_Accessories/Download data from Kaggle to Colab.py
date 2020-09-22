"""
How to download datasets from Kaggle and run into colab
"""

# install the depondencies
! pip install kaggle

from google.colab import files
files.upload()

! mkdir -p ~/.kaggle
! cp kaggle.json ~/.kaggle/

! chmod 600 ~/.kaggle/kaggle.json

! kaggle datasets download -d paultimothymooney/chest-xray-pneumonia

! pip install zip_files

from zipfile import ZipFile
file_name = '/content/chest-xray-pneumonia.zip'
with ZipFile(file_name,'r') as zip:
  zip.extractall()
  print('Done')
