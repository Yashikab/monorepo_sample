from logging import getLogger
from typing import Dict

import pandas as pd

logger = getLogger(__name__)

def generate_df(data: Dict[str, list]):
    # add some command
    logger.info("Create Dataframe.")
    return pd.DataFrame(data)
