from django.contrib.syndication.views import Feed
from ablog.models import Entry

class LatestPosts(Feed):
    title = "ab Blog"
    link = "/feed/"
    description = "Latest Posts"

    def items(self):
        return Entry.objects.published()[:5]
