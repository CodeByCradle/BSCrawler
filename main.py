import argparse
import requests

from bs4 import BeautifulSoup as bs

from helper import create_filename_from_link


# actually, I should make a class, or should I?? don't know.... ok. I need to make a class 

class WebCrawler:
    def __init__(self, web_link:str, filename_stem:str):
        self.web_link: str = web_link 
        self.filename_stem: str = filename_stem

    def test(self):
        # too early to remove it XD
        print(f"{self.web_link} and {self.filename_stem}")
        
    def get_material(self): 
        """download material from a given web page link and save it 

        Args:
            web_link (str): a given web page link. 
        """
        r = requests.get(self.web_link)
        if r.status_code == 200:
            # if the web page link is valid/responding. 
            with open(f"Data/{self.filename_stem}", "w") as xml_file:
                xml_file.write(r.text)
            return True
        return False

    def extract_data(data_path: str):
        """Parse xml and save in a nested array. Yes, it is stupid to save it as a nested array. But we can change it later XD

        Args:
            data_path (str): a data path where I save my downloaded data. 

        Returns:
            array : a nested array.
        """
        # parse xml. Later, we need to try to download the xml from a given link.
        with open(data_path) as f:
            data = f.read() 
        bs_data = bs(data, "xml")
        # Japhug, later will probably use another language. 
        phono_forms =bs_data.find_all("FORM") 
        jap_material = [phono_form.text for phono_form in phono_forms] # coooooool. I get only the content and the tag is removed. 
        # Franch
        translation = bs_data.find_all("TRANSL")
        translation_material = [sentence.text for sentence in translation]
        return [jap_material, translation_material]


    def write_data_to_file(input_array, output_filename):
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
    test = wc.get_material()
    print(test)
    # jap_fr_arrays = extract_data("Data/three_sisters.xml") # did I give the wrong path XD
    # # this should work, in theory....
    # write_data_to_file(jap_fr_arrays[0], "jap_three_sisters.txt")
    # write_data_to_file(jap_fr_arrays[1], "fr_three_sisters.txt")
    # for idx, value in jap_fr_dictionary.items():
