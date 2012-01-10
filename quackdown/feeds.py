'''Processes rss and atom feeds for pubman Articles.
'''

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.utils.translation import ugettext as _

from models import Claim, Response

class LatestClaimsAndResponsesRSSFeed(Feed):
    title = _("Quackdown")
    link = "/claimsandresponses/"
    description = _("Latest claims and responses")

    def items(self):
        def sort_by_date(obj):
            return obj.date_added

        claims = Claim.objects.all()
        responses = Response.objects.all()

        objects = (list(claims) + list(responses))

        if objects:
            objects.sort(key=sort_by_date, reverse=True)

        return objects

    def item_title(self, item):
        return item.__unicode__()

    def item_description(self, item):
        return item.short_description

class LatestClaimsAndResponsesAtomFeed(LatestClaimsAndResponsesRSSFeed):
    feed_type = Atom1Feed

    def item_description(self, item):
        return item.short_description
