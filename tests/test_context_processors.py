import django

from amikeco import context_processors


def test_django_version():
    """Test the django_version context processor.

    Must return a dictionary containing the current Django version.
    """
    assert context_processors.django_version(None) == {'django_version': django.get_version()}
