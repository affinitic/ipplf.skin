from plone.theme.interfaces import IDefaultPloneLayer
from zope.interface import Interface


class ICustomTheme(IDefaultPloneLayer):
    """
    Theme for cesstex
    """


class IInfoHomePage(Interface):
    """
    Gestion des news infos semaine sur la folder view
    """

    def getNews():
        """
        liste les news
        """

    def getNewsIconURL(newsBrain):
        """
        recupere l'icone d'une news (ou celle par defaut)
        """
