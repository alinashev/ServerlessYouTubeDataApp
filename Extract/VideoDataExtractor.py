import logging
from typing import Any

from Settings import youTubeAPIsettings
from googleapiclient.discovery import build
from Extract.DataExtractor import DataExtractor


class VideoDataExtractor(DataExtractor):

    def __init__(self, key=youTubeAPIsettings.key) -> None:
        self.__youtube: Any = build('youtube', 'v3', developerKey=key)

    def extract(self, ChannelsID: dict) -> dict:
        list_req: list = list()
        for channelID in ChannelsID:
            request = self.__youtube.search().list(
                part="snippet",
                channelId=ChannelsID[channelID],
                maxResults="5",
                order="rating"
            )
            response: Any = request.execute()
            list_req.append(response)
        logging.info("Data about video pulled")
        return dict(zip(list(map(lambda c: c, ChannelsID)), list_req))