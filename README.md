# Text to speech model for endangered language
**Kindly note that this is my personal practice repository, where I regularly update the code during my Twitch streaming sessions. If you're intrigued by this project, feel free to join the stream or leave a comment in the issues section**

Delve into the world of linguistic diversity with my project, where I harness the power of Beautiful Soup to gracefully scrape data from the Pangloss website. By parsing the XML files retrieved, I meticulously construct a comprehensive data frame, serving as the backbone for my linguistic exploration.

But that's not all - I extend this venture beyond data collection. Leveraging the audios also sourced from Pangloss, I seamlessly clip them using the information stored in the data frame. These snippets become invaluable assets as I fine-tune a state-of-the-art text-to-speech model.

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
