from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from . import creator_bp, creator_forms
from app import models


@creator_bp.route("/me")
@login_required
def home():
    author_articles = models.Article.get_articles_by_author(current_user.id)

    return render_template("creator/creator_home.html", articles=author_articles)


@creator_bp.route("/me/articles/new", methods=["GET", "POST"])
@login_required
def new_post():
    form = creator_forms.PostForm()
    if request.method == "POST":
        models.Article.insert_article(form, current_user.id)

        return redirect(url_for('creator_bp.home'))

    return render_template("creator/creator_new_post.html", form=form)


@creator_bp.route("/me/articles/edit/<int:article_id>", methods=["GET", "POST"])
@login_required
def edit_article(article_id):
    if request.method == 'POST':
        form = creator_forms.PostForm()    
        if form.validate():
            print('validated form.')
            models.Article.update_article(article_id, form) 

            return redirect(url_for("creator_bp.home"))
    
    article_from_db = models.Article.get_article(article_id)
    article = { "title":article_from_db.title, "subtitle":article_from_db.subtitle, "content":article_from_db.content_markdown, 
                "date":article_from_db.posted_date, "author":current_user.id, "archived":article_from_db.archived }

    # pre-populate the form with data from the article
    form = creator_forms.PostForm(**article)
    return render_template("creator/creator_edit_article.html", article=article, form=form)

