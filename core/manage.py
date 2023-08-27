import click
from flask.cli import with_appcontext


@click.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from core.extensions import db
    from core.models import User

    click.echo("create user")
    user = User.query.filter_by(username="admin").first()
    if user:
        click.echo("Admin user exists skippping init")
        return

    user = User(
        username="admin", email="jithintom1@gmail.com",
        password="admin", active=True
    )
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")
