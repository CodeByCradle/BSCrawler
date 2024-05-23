# BSParser
Using beautifulsoup to parse xml files downloded from Pangloss and extract the phonological data and translation from the input file. 

# How to use 

Create a virtual environment and install relavent packages via **pip**. Please note that the **nlpenv** contains many libraries that will be used for **natural language processing**

```
$ python3 -m venv nlpenv
$ source nlpenv/bin/activate 
$ python3 -m pip install -r requirements.txt
```

Create a file contains many web links from **[Pangloss](https://pangloss.cnrs.fr/)**. See the file **example.txt**

```
https://cocoon.huma-num.fr/data/jacques/masters/crdo-JYA_LWLU.xml
https://cocoon.huma-num.fr/data/jacques/masters/crdo-JYA_DIVINATION.xml
https://cocoon.huma-num.fr/data/jacques/masters/crdo-JYA_LOBZANG.xml
```

Execute the script using the commandline

```
$ python3 main.py [input_file] [data_folder]
```

For example, 

```
python3 main.py example.txt Data
```