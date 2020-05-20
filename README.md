# StackOverflow/StackExchange data dumps to MongoDB (via Python)

Python script to load StackOverflow (or any other StackExchange website) dump to MongoDB instance for ease of access.  
Dumps are available at https://archive.org/details/stackexchange.

## Steps

1. Download the data. Tip: You can use `axel` to increase your download speed
  ```bash
  # instructions for using it on macOS
  
  # install axel with brew
  brew install axel
  
  # downloads with 16 simultaneous connections
  axel -n 16 <link> 
  ```
2. Unzip the `7z` file to get the `XML`s and structure it as mentioned inside the `data` directory
3. Install the python dependencies, by running `pip install -r requirements.txt` (from inside the `code` directory)
4. In the script `import_to_mongo.py`, edit lines [9](https://github.com/Daksh/stackoverflow-dump-to-mongodb/blob/master/code/import_to_mongo.py#L9), [10](https://github.com/Daksh/stackoverflow-dump-to-mongodb/blob/master/code/import_to_mongo.py#L10), [15](https://github.com/Daksh/stackoverflow-dump-to-mongodb/blob/master/code/import_to_mongo.py#L15) to set which StackExchange Network's data you wish to process, which database name to use in MongoDB and which files from that network you wish to import. 
5. Set the data path in `utils.py`, [line 3](https://github.com/Daksh/stackoverflow-dump-to-mongodb/blob/master/code/utils.py#L3)
6. Simply run the `import_to_mongo.py` script. It even shows a progress bar indicating the number of processed entry from each file to be imported.

## Experiments

There are two Jupyter notebooks in `code/misc/`. You can play around with the `experiments_import_to_mongo.ipynb` file to understand/change how we import the data to Mongo. If you wish to index the data in MongoDB, please have a look at `index_mongodb.ipynb`
