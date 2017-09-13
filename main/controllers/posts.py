from flask import Blueprint, render_template, abort
from ..models.post import Post

posts = Blueprint('posts', __name__)


@posts.route('/posts/<id>')
def post(id):
    data = {}
    post = Post.query.get_or_404(id)
    if not post:
        abort(404)
    data = {'id': post.id,
            'body': post.body,
            'timestamp': post.timestamp,
            'username': post.users.username,
            'title': post.title
            }
    return render_template('post.html', post=data)


'''
# to use in html template:
# <h4>{{ product|full_name }}</h4>
@post.app_template_filter('full_name')
def full_name_filter(resort):
    return '{0} / {1}'.format(resort['name'],
                              resort['category'])


@resorts.app_template_filter('format_currency')
def format_currency_filter(amount):
    currency_code = ccy.countryccy(request.accept_languages.best[-2:])
    return '{0} {1}'.format(currency_code, amount)


# to use in html template:
# simply call <h4>{{ full_name(product) }}</h4>
@resorts.context_processor
def some_processor():
    def full_name(product):
        return '{0} / {1}'.format(resorts['category'],
                                  resorts['name'])

    return {'full_name': full_name}
'''