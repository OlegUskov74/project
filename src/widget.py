import masks
from typing import Union

def mask_account_card(type_card_or_account_number: Union[str, int]) -> str:
    """функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""


    pass


from datetime import datetime


def get_date(my_date: str) -> str:
    """функция, которая возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    date_obj = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


print(get_date("2024-03-11T02:26:18.671407"))
