import argparse
import requests
from pathlib import Path

from bs4 import BeautifulSoup as bs
from lxml import etree  # try this one to work on the lang tag

from helper import create_input_output_pairs


# actually, I should make a class, or should I?? don't know.... ok. I need to make a class


class WebCrawler:
    def __init__(self, web_link: list, filename_stem: list):
        """initiation.

        Args:
            web_link (str): _description_
            filename_stem (str): _description_
        """
        self.web_link: list = web_link
        self.filename_stem: list = filename_stem

    def get_material(self, data_dir: str):
        """Download material from a given web page link and save it

        Returns:
            str: a file path
        """
        print(f"Current web link is {self.web_link}")
        r = requests.get(self.web_link)
        if r.status_code == 200:
            with open(f"{data_dir}/{self.filename_stem}", "w") as xml_file:
                xml_file.write(r.text)
            return f"{data_dir}/{self.filename_stem}"
        else:
            print(r.status_code)
            # This is so stupid. It should work without this else!
            return None

    def extract_by_tag(slef, data_path: str, tag: str):
        """Extract the data according to a given tag from the given data path. I decide to move the language tag recognition to later.

        Returns:
            list: an array contains all the sentences.
        """
        try:
            with open(data_path) as f:
                bs_data = bs(f.read(), "xml")
                tag_data = bs_data.find_all("S")
                total_text = []
                for each_td in tag_data:
                    middle_process = each_td.find_all(tag, recursive=False)
                    total_text.extend([sentence.text for sentence in middle_process])
                return total_text
        except Exception as e:
            print(f"error is {e}")

    def write_data_to_file(self, input_array, output_filename):
        """Write the form and translation data to file

        Args:
            input_array (list): The form or translation
            output_filename (str): The output file name, the stem, not the .txt or something.
        """
        with open(output_filename, "w") as output:
            for each_sentence in input_array:
                output.write(each_sentence + "\n")


if __name__ == "__main__":
    # TODO: find a better way to reduce this argument parser.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file", help="Please give a file contains multiple web links."
    )
    # TODO: add an option to take webpage link directly.
    parser.add_argument("data_dir", help="Please give a directory to store the data")
    args = parser.parse_args()
    data_pairs = create_input_output_pairs(args.input_file)
    data_dir = Path(args.data_dir).mkdir(parents=True, exist_ok=True)
    for filename, link in data_pairs.items():
        wc = WebCrawler(link, filename)
        xml_file_path = wc.get_material(data_dir)
        if xml_file_path:
            for tag in ["FORM", "TRANSL"]:
                the_text = wc.extract_by_tag(Path(xml_file_path).as_posix(), tag)
                wc.write_data_to_file(
                    the_text, f"{data_dir}/{tag.lower()}_{filename}.txt"
                )
