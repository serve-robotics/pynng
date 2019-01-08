import importlib.machinery
import importlib.util
import os

import pynng._nng
this_dir = os.path.dirname(os.path.abspath(__file__))
path = pynng._nng.__file__
name = '_nng_extra'
loader = importlib.machinery.ExtensionFileLoader(name, path)
spec = importlib.util.spec_from_loader(name, loader)
module = importlib.util.module_from_spec(spec)
loader.exec_module(module)

