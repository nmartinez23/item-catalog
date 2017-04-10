from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, LatestItem, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


User1 = User(name="Nick Martinez", email="23nickmartinez@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/' +
             '18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

category1 = Category(user_id=1, name="Surfing")

session.add(category1)
session.commit()

latestItem1 = LatestItem(user_id=1, name="Surfboard",
                         description="Catch waves all day with this " +
                         "killer board!", category=category1)

session.add(latestItem1)
session.commit()


latestItem2 = LatestItem(user_id=1, name="Wetsuit",
                         description="Stay warm and protected from " +
                         "the cold water", category=category1)

session.add(latestItem2)
session.commit()


category2 = Category(user_id=1, name="Snowboarding")

session.add(category2)
session.commit()


latestItem1 = LatestItem(user_id=1, name="Snowboard",
                         description="Tear up the slopes and " +
                         "possibly get a concussion with this sweet ride",
                         category=category2)

session.add(latestItem1)
session.commit()

latestItem2 = LatestItem(user_id=1, name="Snowboard Boots",
                         description="Ride in comfort with tough yet " +
                         "flexible boots", category=category2)

session.add(latestItem2)
session.commit()

print "added new items"
