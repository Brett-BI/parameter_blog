from datetime import datetime
from flask_login import UserMixin

from app import db


# USER MODELS
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    user_email = db.Column(db.String(120), nullable=False)
    user_password = db.Column(db.String(200), nullable=False)


# WRITER MODELS
class Writer(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    writer_user_id = db.Column(db.Integer(), db.ForeignKey(User.id), nullable=False) # foreign key ref too
    writer_about_me = db.Column(db.String(200))
    writer_short_summary = db.Column(db.String(40))


# POST MODELS
class Post(db.Model):
    post_id = db.Column(db.Integer(), primary_key=True)
    author_id = db.Column(db.Integer())
    post_title = db.Column(db.String(length=200))
    post_subtitle = db.Column(db.String(length=300))
    post_content = db.Column(db.Text())
    post_date = db.Column(db.DateTime())
    post_was_edited = db.Column(db.Boolean())
    post_archived = db.Column(db.Boolean())

    @classmethod
    def insert_post(cls, post_form):
        # should probably not presume the data is ok at this point but for now, we will
        # will need to add additional logic here later to ensure that the post object is correct

        # create the Post object from the PostForm object
        new_post = cls(post_title=post_form.title.data, post_subtitle=post_form.subtitle.data,
        post_content=post_form.content.data, post_date=post_form.date.data, post_archived=post_form.archive.data)

        print(new_post)        
        db.session.add(new_post)
        db.session.commit()
    
    @staticmethod
    def _get_post(post_id):
        post = Post.query.filter_by(post_id=post_id).first()

        return post

    def __repr__(self):
        return "<Post: {}>".format(self.post_title)