import pandas as pd



def unique_mails(excelfile: str):
  df = pd.read_excel(excelfile)

  unique_values = df.mail.unique()

  return unique_values

