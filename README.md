# Computer Infrastructure Assessment
Assessed work for the Computer Infrastructure module, part of the Higher Diploma in Data Analytics course at Atlantic Technological University, Ireland, Autumn 2025 
author: Susan Collins
The assessment instructions fulfilled in this repository are listed here: [assessment.md](https://github.com/ianmcloughlin/computer-infrastructure/blob/main/assessment/assessment.md)


## Description of this repository
This repo contains code to download hourly stock prices, for the last 5 days, 
for the 5 FAANG companies listed on NASDAQ (META, AAPL, AMZN, NFLX, GOOG).  
This data is stored as a CSV file with a timestamped filename, 
then re-ingested and exported as a PNG plot.  
The Python script [`faang.py`](https://github.com/SuColl/computer-infrastructure-assessment/blob/main/faang.py) 
performs all the above tasks.  
The GitHub Action Workflow dscribed in [`faang.yml`](https://github.com/SuColl/computer-infrastructure-assessment/blob/main/.github/workflows/faang.yml) automatically runs `faang.py` on Saturday mornings.  
The Jupyter notebook [`problems.ipynb`](https://github.com/SuColl/computer-infrastructure-assessment/blob/main/problems.ipynb) 
breaks down and explains each part of the code, with additional analysis.


## Repository structure
├── [data/](https://github.com/SuColl/computer-infrastructure-assessment/blob/data/)  
│   ├── [20251220-092224.csv](https://github.com/SuColl/computer-infrastructure-assessment/blob/data/20251220-092224.csv)  
│   ├── [20251220-200119.csv](https://github.com/SuColl/computer-infrastructure-assessment/blob/data/20251220-200119.csv)  
├── [plots/](https://github.com/SuColl/computer-infrastructure-assessment/blob/plots/)  
│   ├── [20251220-200119.csv](https://github.com/SuColl/computer-infrastructure-assessment/blob/data/20251220-200119.csv)  
│   ├── [20251220-092224.png](https://github.com/SuColl/computer-infrastructure-assessment/blob/data/20251220-092224.png)  
│   ├── [20251220-200119.png](https://github.com/SuColl/computer-infrastructure-assessment/blob/data/20251220-200119.png)  
├── [faang.py](https://github.com/SuColl/computer-infrastructure-assessment/blob/main/faang.py)  
├── [problems.ipynb](https://github.com/SuColl/computer-infrastructure-assessment/blob/main/problems.ipynb)  
├── [README.md](https://github.com/SuColl/computer-infrastructure-assessment/blob/main/README.md)  
└── [requirements.txt](https://github.com/SuColl/computer-infrastructure-assessment/blob/main/requirements.txt)  
├── .github/  
│   ├── faang.yaml  
├── .gitignore  



## Files in this repository
[README.md](https://github.com/SuColl/computer-infrastructure-assessment/blob/main/README.md)  - this file

[.gitignore](https://github.com/SuColl/computer-infrastructure-assessment/blob/main/.gitignore) - a standard Git configuration file to prevent the upload of unnecessary files to the repository

[requirements.txt](https://github.com/SuColl/computer-infrastructure-assessment/blob/main/requirements.txt) - a list of Python libraries required to run the code in the Juypter notebook

[problems.ipynb](https://github.com/SuColl/computer-infrastructure-assessment/blob/main/problems.ipynb) - the Jupyter notebook containing code cells, results, explanatory notes and analyses


## Libraries required
- Python builtin modules
  - [datetime](https://docs.python.org/3/library/datetime.html) to handle date and time data
  - [os](https://docs.python.org/3/library/os.html) to interface with the operating system
  - [re](https://docs.python.org/3/library/re.html) to use regular expressions, used for string matching 
- Data manipulation
  - [NumPy](https://numpy.org/doc/stable/ )
  - [Pandas](https://pandas.pydata.org/docs/) Python Data Analysis Library
- Data Visualisation
  - [Matplotlib.PyPlot](https://matplotlib.org/stable/api/pyplot_summary.html) for plotting
- Data Acquisition
  - [yfinance](https://github.com/ranaroussi/yfinance) accessing financial data for these exercises



## Expected output
```console
$ ./faang.py
[*********************100%***********************]  5 of 5 completed
Downloaded DataFrame Shape: 
 (35, 25)
Directory exists at data/
Current date and time are 2025-12-21 01:57:53.858452.
Generated CSV filename is 20251221-015753.csv.
Data written to data/20251221-015753.csv
Directory exists at data/
Directory data/ contains 25 files with appropriate filenames: the latest one is 20251221-015753.csv.
Read in: data/20251221-015753.csv
Plot created at plots/20251221-015753.png
```

## Sample output plot
<img src="plots/20251220-092224.png" width="800">


## Setup - To Run in Github Codespace
1. Sign up for a free Github account.
2. Go to the repository page in your browser.
3. Click the green Code button.
4. Click the Codespaces tab.
5. click Create New Codespace on main.

## Technologies used in the creation of this repository
- Python v3.12.1
- Git
- GitHub
- Codespaces
- Jupyter