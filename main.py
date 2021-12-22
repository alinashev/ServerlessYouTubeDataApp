from Commons.ChannelsID import ChannelsID
from Commons.FileWriter import FileWriter
from Commons.ReaderJSON import ReaderJSON
from Commons.StorageS3 import StorageS3
from Extract.ChannelDataExtractor import ChannelDataExtractor
from Extract.VideoCategoryExtractor import VideoCategoryExtractor
from Extract.VideoDataExtractor import VideoDataExtractor
from Transform.VideoIDParser import VideoIDParser


def main():
    storage: StorageS3 = StorageS3()
    extractor_channels: ChannelDataExtractor = ChannelDataExtractor()
    extractor_videos: VideoDataExtractor = VideoDataExtractor()

    channel_file_name = 'dataChannels.json'
    video_file_name = 'dataVideos.json'

    file_writer_channels: FileWriter = FileWriter(channel_file_name)
    file_writer_videos: FileWriter = FileWriter(video_file_name)

    channel_id: dict = ChannelsID('channels.txt').get_channels_id()

    file_writer_channels.writing(extractor_channels.extract(channel_id))
    print("dataChannels wrote")

    file_writer_videos.writing(extractor_videos.extract(channel_id))
    print("dataVideos wrote")

    reader_video: ReaderJSON = ReaderJSON('dataVideos.json')
    json_video: dict = reader_video.get_json()

    video_id: list = VideoIDParser().parse(json_video, channel_id)

    video_category_extractor: VideoCategoryExtractor = VideoCategoryExtractor()

    file_writer_category: FileWriter = FileWriter('videoCategory.json')
    file_writer_category.writing(video_category_extractor.extract(video_id))

    storage.upload(file_writer_channels.get_path())
    storage.upload(file_writer_videos.get_path())
    storage.upload(file_writer_category.get_path())


if __name__ == '__main__':
    main()
