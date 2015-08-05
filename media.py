import webbrowser


class Movie(object):
    """Data structure to hold movie information."""
    def __init__(self, title, storyline, poster_image_url, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        """Opens a browser and goes to the trailer url that was passed
        into the constructor.
        """
        webbrowser.open(self.trailer_url)
