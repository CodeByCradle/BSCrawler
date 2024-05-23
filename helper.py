def create_filename_from_link(web_link: str):
    """Create a filename from a given web link. Ok.... the function sounds so stupid...

    Args:
        web_link (str): a given web link
    """
    filename = web_link.split("/")
    # usually web_link.split("/")[-1] should really work 
    return filename[-1] 

def create_input_output_pairs(filename: str):
    """Create a pair with input link and output file name

    Args:
        filename (str): a file with multiple links. 

    Returns:
        dict: a dictionary with a structure like {"filename": "links"}
    """
    with open(filename, "r") as input_file:
        links = input_file.readlines()
        print(links)
        file_pairs = {}
        for link in links:
            link = link.strip("\n")
            filename = create_filename_from_link(link)
            file_pairs[filename] = link
        return file_pairs
    