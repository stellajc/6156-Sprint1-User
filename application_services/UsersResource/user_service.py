from application_services.BaseApplicationResource import BaseRDBApplicationResource
from database_services.RDBService import RDBService as RDBService

# data schema: UserInfo
# table_name: Users
class UserResource(BaseRDBApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_links(cls, resource_data):
        pass

    @classmethod
    def find_by_template(cls, template, limit, offset):
        res = RDBService.find_by_template("UserInfo", "User", template, limit, offset)
        return res

    @classmethod
    def create(cls, create_data):
        res = RDBService.create("UserInfo", "User", create_data)
        return res

    @classmethod
    def update(cls, select_data, update_data):
        res = RDBService.update("UserInfo", "User", select_data, update_data)
        return res

    @classmethod
    def delete(cls, template):
        res = RDBService.delete("UserInfo", "User", template)
        return res
