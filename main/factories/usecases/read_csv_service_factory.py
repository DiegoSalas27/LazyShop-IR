from domain.usecases.read_csv import ReadCsv
from infrastructure.pandas.pandas_adapter import PandasAdapter
from services.usecases.read_csv_service import ReadCsvService


def makeReadCsvService() -> ReadCsv:
  fileManager = PandasAdapter()
  return ReadCsvService(fileManager)