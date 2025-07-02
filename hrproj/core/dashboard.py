from grappelli.dashboard import Dashboard, modules

class CustomIndexDashboard(Dashboard):
    """
    Custom Grappelli “home page” dashboard.
    """
    def init_with_context(self, context):
        # 1) A row of “quick links”:
        self.children.append(modules.LinkList(
            title="Quick links",
            layout="inline",            # horizontal list
            children=[
                {'title': 'Site Home', 'url': '/', 'external': False},
                {'title': 'Django Docs', 'url': 'https://docs.djangoproject.com/', 'external': True},
            ]
        ))

        # 2) A list of your apps / models:
        self.children.append(modules.ModelList(
            title="Core Models",
            models=('core.models.Organization', 'core.models.Employee'),
        ))

        # 3) Recent admin actions:
        self.children.append(modules.RecentActions(
            title="Recent Actions",
            limit=5,
        ))
