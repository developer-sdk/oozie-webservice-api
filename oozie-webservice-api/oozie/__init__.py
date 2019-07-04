from .oozie import Admin, Versions, Job, Jobs

class OozieWebService(object):
    
    def __init__(self, oozie_url):
        self._OOZIE_URL = oozie_url
        
        self.admin = Admin(oozie_url)
        self.version = Versions(oozie_url)
        self.job = Job(oozie_url)
        self.jobs = Jobs(oozie_url)