
# Online Learning Course EDA Based on CRISP-DM

Based on First-Three-Stage of CRISP-DM Model, using data from Cyber Security online learning course, do some EDA.

## Requirement

0. pip2/pip3 install the packages in ./requirement.txt
1. If there is a error because of the API,so you need go to the plotly official website-->signin(username:haoranduan28@gmail.com, password:plotly123)-->click right corner name-->setting-->click left side API Keys-->Regenerate API-->Get a API key(remeber this step)
2. Find the code 'plotly.tools.set_credentials_file(username='haoran88', api_key='o8i3aa8qgpoIpCOBQgt8')' in each '.py' and '.ipynb' file and change the API Keys from Requirement3.
3. Go to google to get a google free API.(AIzaSyB2DKOMtZVdPBThMcJyWZhnyTvdrn_HuRo)
4. Follow https://github.com/pbugnion/gmaps to install the dependences for jupyter notebook

## Usage

- *Note : In this data science project,there are some functions in each .py file, they can re-use for the same process in differet kind of single file in same project.

- Step 1 : In this project, we don't need to run any .py file except the 'Unittest'. All the operation and analysis will present in jupyter notenook which is './notebook/CRISP-DM.ipynb'-------------Please use jupyter note book to open it after finishing the Requirement successfully.

- Step 2 : There is a button before 'Data Understanding', if you don't want to see any code but just focus on analysising, you can click the button to hide or show them

- Step 3 : Go to the './src/Unit_Test/' use commend:
pytest test.py
