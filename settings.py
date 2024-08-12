class Settings:
    _project_url = 'https://stellarburgers.nomoreparties.site'

    @property
    def base_url(self):
        return self._project_url


base_url = Settings().base_url
