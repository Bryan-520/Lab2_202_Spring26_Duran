from dataclasses import dataclass
from typing import TypeAlias

Price: TypeAlias = float
Date: TypeAlias = str

@dataclass
class StockRecord:
    open_price: Price  
    close_price: Price  
    date: Date         

StockData: TypeAlias = list[StockRecord]   
WeeklyAverages: TypeAlias = list[Price]    