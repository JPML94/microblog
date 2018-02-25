from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from app import db
from app.feedback.forms import FeedbackForm
from app.main.forms import SearchForm
from app.models import User, FeedbackPost
from app.feedback import bp

@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
        g.search_form = SearchForm()
    g.locale = str(get_locale())

@bp.route('/feedbackform', methods=['GET', 'POST'])
@login_required
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        feedbackPost = FeedbackPost(        
        cohort = form.cohort.data,
        track = form.track.data,
        curriculumGrade = form.curriculumGrade.data,
        curriculumComment = form.curriculumComment.data,
        projectGrade = form.projectGrade.data,
        projectComment = form.projectComment.data,
        carDevGrade = form.carDevGrade.data,
        carDevComment = form.carDevComment.data,
        overallGrade = form.overallGrade.data,
        overallComment = form.overallComment.data)
        db.session.add(feedbackPost)
        db.session.commit()
        flash(_('Thanks for submitting your feedback!'))
        return redirect(url_for('main.index'))
    return render_template('feedback.html', title=_('Feedback'), form=form)