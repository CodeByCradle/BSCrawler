import argparse
import requests
from pathlib import Path 

from bs4 import BeautifulSoup as bs

from helper import create_filename_from_link


# actually, I should make a class, or should I?? don't know.... ok. I need to make a class 

class WebCrawler:
    def __init__(self, web_link:str, filename_stem:str):
        self.web_link: str = web_link 
        self.filename_stem: str = filename_stem

    def test(self):
        # soon we will remove it
        print(f"{self.web_link} and {self.filename_stem}")
        
    def get_material(self): 
        """Download material from a given web page link and save it 

        Returns:
            str: a file path
        """
        r = requests.get(self.web_link)
        if r.status_code == 200:
            # if the web page link is valid/responding. Here, it is not so good to hard code the path ("Data") because we **might** change it in the future.
            # TODO: find a solution for the data path. 
            with open(f"Data/{self.filename_stem}", "w") as xml_file:
                xml_file.write(r.text)
            return f"Data/{self.filename_stem}"
        return None
    
    def extract_by_tag(slef, data_path:str, tag: str):
        """Extract the data according to a given tag from the given data path.

        Returns:
            list: an array contains all the sentences. 
        """
        try: 
            with open(data_path) as f:
                data = f.read() 
                bs_data = bs(data, "xml")
                tag_data = bs_data.find_all(tag) 
                #TODO: find only the sentence, do not find the form or translation under the word <W> tag
                _text =  [sentence.text for sentence in tag_data if sentence.find_parent("S")]  
                return _text
        except Exception as e:
            print(f"error is {e}")
            

    def write_data_to_file(self, input_array, output_filename):
        with open(output_filename, "w") as output:
            for each_sentence in input_array:
                output.write(each_sentence+"\n")


if __name__ == "__main__":
    # initiate the argument parser. I should move this to another place later. 
    parser = argparse.ArgumentParser()
    parser.add_argument("link", help="Please give a webpage link") 
    args = parser.parse_args()
    #"https://cocoon.huma-num.fr/data/jacques/masters/crdo-JYA_DELUGE.xml"
    filename = create_filename_from_link(args.link)
    wc = WebCrawler(args.link, filename)
    xml_file_path = wc.get_material()
    for tag in ["FORM", "TRANSL"]:
        the_text = wc.extract_by_tag(Path(xml_file_path).as_posix(), tag) 
        print(the_text)
    # # this should work, in theory....
    # write_data_to_file(jap_fr_arrays[0], "jap_three_sisters.txt")
    # write_data_to_file(jap_fr_arrays[1], "fr_three_sisters.txt")
    # for idx, value in jap_fr_dictionary.items():
