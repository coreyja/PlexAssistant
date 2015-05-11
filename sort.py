__author__ = 'coreyja'

from datetime import datetime

class Sorter():

    def __init__(self):
        self.scorers = [
            LastViewedScorer(),
            ViewCountScorer(),
        ]

    def sort(self, videos):
        for video in videos:
            video.score = 0;
            for scorer in self.scorers:
                video.score += scorer.score(video)

        videos.sort(key=lambda x: x.score, reverse=True)


class Scorer():

    def __init__(self):
        pass

    def score(self, video):
        pass


class LastViewedScorer(Scorer):

    def score(self, video):
        now = datetime.now();
        if video.lastViewedAt is None:
            return 1000
        return (now - video.lastViewedAt).days


class ViewCountScorer(Scorer):

    def score(self, video):
        return -video.viewCount