# Nestor Mejia - Technical assessment

## Installation
The tool requires a python 3.10 installation.

To install the dependencies to the base python 3.10 installation (or virtual environment) cd into `./server` and run `pip install -r requirements.txt`.

Once installed, to parse the raw data from the json files (and while at the server directory) run `python parse_raw_data.py` , the script will take a while to process and store the data to a sqlite database called `f1_data.db` and will be stored to the `./server` directory.

## Usage
After installing the dependencies and running the parser script, run `python main.py` from the `./server` directory.

## API
All the requirements are exposed via graphql, to retrieve the data, visit `http://localhost:8000/graphql` (or use any graphql query program like Postman or Altair) to access the Graphql API. Fetching the schema will list all available endpoints and their object definitions.

## User Interface
A small frontend project has been created using Vue3, to check the files, please navigate to the `./frontend` directory. To access the UI, head to `http://localhost:8000` where the bundled UI should be available.
You'll be presented with a dropdown to select a race and the driver standings for that specific race will be shown, clicking on any driver on the table will display the driver details and driver summary to the right of the table.