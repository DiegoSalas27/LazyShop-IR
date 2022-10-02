from pandas import DataFrame
from domain.usecases.read_csv import ReadCsv
from services.protocols.file_manager import FileManager


# this class implements the read csv interface
class ReadCsvService(ReadCsv):
  def __init__(self, fileManager: FileManager):
    self.fileManager = fileManager
  
  def read_csv(self, filename: str, encoding: str) -> DataFrame:
    sentence_doc = self.fileManager.read_csv(filename, encoding)

    return sentence_doc