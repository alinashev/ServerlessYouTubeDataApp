import logging
from Settings import youTubeAPIsettings

from typing import Any
from googleapiclient.discovery import build
from Extract.DataExtractor import DataExtractor


class ChannelDataExtractor(DataExtractor):

    def __init__(self, key=youTubeAPIsettings.key) -> None:
        self.__youtube: Any = build('youtube', 'v3', developerKey=key)

    def extract(self, ChannelsID: dict) -> dict:
        list_req: list = list()
        for channelID in ChannelsID:
            request: Any = self.__youtube.channels().list(
                part="statistics",
                id=ChannelsID[channelID]
            )
            response = request.execute()
            list_req.append(response)
        logging.info("Data about channels pulled")
        return dict(zip(list(map(lambda c: c, ChannelsID)), list_req))
