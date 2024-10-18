import numpy as np
import pandas as pd
from  ydata_profiling import ProfileReport

df = pd.read_csv("results.csv")

profile = ProfileReport(df, title="Football Report")

profile.to_file('results_report.html')