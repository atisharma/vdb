from hyjinx import config

from pathlib import Path
from platformdirs import user_state_path, user_config_path


cfg = {"embeddings.model": "all_mpnet_base_v2",
       "path": Path(user_state_path("vdb"), "default.vdb")}

try:
    cfg = {** cfg,
           ** config(Path(user_config_path("vdb"), "config.toml"))}
except FileNotFoundError:
    pass
