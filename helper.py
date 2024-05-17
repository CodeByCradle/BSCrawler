
def create_filename_from_link(web_link: str):
    """Create a filename from a given web link. Ok.... the function sounds so stupid...

    Args:
        web_link (str): a given web link
    """
    filename = web_link.split("/")
    # usually web_link.split("/")[-1] should really work 
    return filename[-1] 