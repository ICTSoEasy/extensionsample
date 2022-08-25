import pkg_resources

__version__ = '0.0.1'

def _jupyter_nbextension_paths():
    return [dict(section="notebook",
                 src="static",
                 dest="extensionsample",
                 require="extensionsample/index")]

def load_jupyter_server_extension(nbapp):
    nbapp.log.info("extensionsample enabled!")