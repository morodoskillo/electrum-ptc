from .version import ELECTRUM_VERSION
from .util import format_satoshis
from .wallet import Wallet
from .storage import WalletStorage
from .coinchooser import COIN_CHOOSERS
from .network import Network, pick_random_server
from .interface import Interface
from .simple_config import SimpleConfig, get_config, set_config
from . import bitcoin
from . import transaction
from . import daemon
from .transaction import Transaction
from .plugin import BasePlugin
from .commands import Commands, known_commands


__version__ = ELECTRUM_VERSION

# This trick allows accessing electrum-ptc from import statements as electrum,
# so we can avoid merge conflicts while also avoiding namespace collisions with
# upstream.
#import pkgutil
#import importlib
#import sys
#electrum-ptc = importlib.import_module('electrum_ptc')
#sys.modules['electrum'] = electrum-ptc
#for _, name, _ in pkgutil.iter_modules(['electrum-ptc']):
#    try:
#        m = importlib.import_module('electrum-ptc' + '.' + name)
#        sys.modules['electrum' + '.' + name] = m
#    except:
#        pass
