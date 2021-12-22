import logging
from typing import Any

from Settings import youTubeAPIsettings
from googleapiclient.discovery import build
from Extract.DataExtractor import DataExtractor


class VideoCategoryExtractor(DataExtractor):

    def __init__(self, key=youTubeAPIsettings.key) -> None:
        self.__youtube: Any = build('youtube', 'v3', developerKey=key)

    def extract(self, video_id_list) -> dict:
        list_response: list = list()
        list_video_id: list = list()

        for video_id in video_id_list:
            request = self.__youtube.videos().list(
                part="id,snippet,statistics",
                id=video_id.get_video_id(),
            )
            response: Any = request.execute()

            list_response.append(response)
            list_video_id.append(video_id.get_video_id())
        logging.info('Data from youtube received')
        return dict(zip(list_video_id, list_response))
