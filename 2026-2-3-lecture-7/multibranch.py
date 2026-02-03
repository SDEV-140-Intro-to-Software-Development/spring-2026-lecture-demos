# Blog post tagging system
# status
    # posts that are 7 days old or less are new
    # posts that are 365 days old or greater are archived
# tags
    # posts that are between 15-31 days old could be marked as a refresher
    # post that is geater 360 days old could be marked as "leaving soon"


age = int(input("> "))

status = None
tags = []

if age <= 7:
    status = "new"
elif age >= 365:
    status = "archived"

if 15<=age<=31:
    tags.append("Good Review Material")

if age>360:
    tags.append("leaving soon")