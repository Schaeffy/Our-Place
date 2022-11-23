from app.models import db, User, BlogPost, Comment, Friendship, FriendRequest


def seed_comments():
    comment1 = Comment(
        user1_id=1,
        user2_id=2,
        comment_body="Hey, what's up?"
    )
    comment2 = Comment(
        user1_id=2,
        user2_id=1,
        comment_body="Yoyoyoyo"
    )

    comment3 = Comment(
        user1_id=1,
        user2_id=3,
        comment_body="Wowza"
    )

    comment4 = Comment(
        user1_id=3,
        user2_id=1,
        comment_body="Hey, I hope you're doing well. it was great seeing you again!"
    )
    comment5 = Comment(
        user1_id=2,
        user2_id=3,
        comment_body="Something is up"
    )

    comment6 = Comment(
        user1_id=2,
        user2_id=3,
        comment_body="There is no spoon"
    )

    comment7 = Comment(
        user1_id=1,
        user2_id=2,
        comment_body="Wow, it's another comment"
    )

    comment8 = Comment(
        user1_id=1,
        user2_id=2,
        comment_body="Quasi Pseudo"
    )

    comment9 = Comment(
        user1_id=2,
        user2_id=1,
        comment_body="Lorem Ipsum"
    )

    comment10 = Comment(
        user1_id=2,
        user2_id=1,
        comment_body="Moooooooooooove on"
    )

    comment11 = Comment(
        user1_id=3,
        user2_id=2,
        comment_body="Don't ghost me"
    )

    db.session.add(comment1)
    db.session.add(comment2)
    db.session.add(comment3)
    db.session.add(comment4)
    db.session.add(comment5)
    db.session.add(comment6)
    db.session.add(comment7)
    db.session.add(comment8)
    db.session.add(comment9)
    db.session.add(comment10)
    db.session.add(comment11)
    db.session.commit()

def undo_comments():
    db.session.execute('TRUNCATE comments RESTART IDENTITY CASCADE;')
    db.session.commit()
