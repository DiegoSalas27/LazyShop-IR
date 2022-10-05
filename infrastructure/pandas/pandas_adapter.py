import pandas as pd
from pandas import DataFrame
from services.protocols.file_manager import FileManager

# this adapter class that implements the FileManager interface
class PandasAdapter(FileManager):

  def read_csv(self, filename: str, encoding: str) -> DataFrame:
    df = pd.read_csv(filename, encoding=encoding)
    return df

  def access_group(self, df: DataFrame, posting_list_combined_for_and_high_priority: list) -> DataFrame:
    df = pd.DataFrame(df.loc[posting_list_combined_for_and_high_priority])
    return df