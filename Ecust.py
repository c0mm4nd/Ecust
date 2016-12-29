# coding: utf8


class Ecust(object):
    """import ME """

    def __init__(self, platform_id, stu_id, stu_pw):
        """
        urp_login Module for the import action
        Args:
            platform_id :
                1 : JWC
                2 : URP
            stu_id : Your Student ID
            stu_pw : Your Student Password of the Student ID
        Return :
            a cookie if it succeed , or False.
        """

        super(Ecust, self).__init__()
        self.platformID = platform_id
        self.stuID = stu_id
        self.stuPW = stu_pw

    def login(self):
        if self.platformID is '1':
            import jwc_login as login
            pass
        elif self.platformID is '2':
            import urp_login as login
        else:
            import sys
            sys.exit("NO LOGIN!")
        login_cookie = login.jwc_login(self.stuID, self.stuPW)
        # print vars(login_cookie)
        return login_cookie
