from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from lbutils import get_or_none

from .leave.models import Leave
from .leave.wfdata import load_data

User = get_user_model()


class BaseTests(TestCase):

    def setUp(self):
        self.init_data()

    def init_users(self):
        def create_user(username, **kwargs):
            return User.objects.create_user(username, "%s@v.cn" % username, 'password', **kwargs)

        super(BaseTests, self).setUp()
        self.users = {
            'owner': create_user('owner'),
            'operator': create_user('operator'),
            'vicalloy': create_user('vicalloy'),
            'tom': create_user('tom'),
            'admin': create_user('admin', is_superuser=True),
        }

    # TODO add a function to submit new leave
    def create_leave(self, reason, submit=True):
        leave = Leave(
            start_on=timezone.now(), end_on=timezone.now(), leave_days=1,
            reason=reason, created_by=self.users['owner'])
        leave.init_actual_info()
        leave.save()
        leave.create_pinstance('leave', submit)
        return leave

    def get_leave(self, reason):
        return get_or_none(Leave, reason=reason)

    def init_leave(self):
        self.leave = self.create_leave('reason', False)

    def init_data(self):
        self.init_users()
        load_data('leave')
        self.init_leave()
