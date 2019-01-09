class TwitterAuthError(Exception):
    def __init__(self, message, detail_json, status_code):
        super().__init__(message)
        self.status_code = status_code
        self.detail_json = detail_json
