from requests import Session
from typing import Dict
from utils import get_tree_from_dict
import json


class ProjectAPI(object):
    def __init__(self,
                 cookie: Dict[bytes, str] = "",
                 header: Dict[dict, None] = None
                 ) -> None:
        """ init fun!!! """
        if header is None:
            self.header = {
                'Cookie': cookie,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61'
            }
        else:
            self.header = header
            self.header['Cookie'] = cookie
        self.session = Session()

    def get_project(self, uid: int) -> dict:
        """
        get project info
        :param uid: project id
        :return: dict, like it: {"name": ..., "main.py": ..., "files": [{"filename": ..., "url": ...], ...}
        """
        res = self.session.get(f"https://code.xueersi.com/api/community/v4/projects/detail?id={uid}&lang=cpp", headers=self.header)
        res = json.loads(res.text)

        if res.get("status") is None:
            return {"message": "操作失败，请检查cookie和作品链接"}

        data = {"name": res["data"]["name"], "main.py": res["data"]["xml"]}
        if res["data"]["assets"].get("assets_url") is None:
            data["assets"] = []
        else:
            origin_assets = self.session.get(res["data"]["assets"]["assets_url"], headers=self.header)
            origin_assets = json.loads(origin_assets.text)["treeAssets"]
            current_path = ""
            assets = []
            get_tree_from_dict(origin_assets, current_path, assets)
    
            data["assets"] = assets
        data["message"] = "操作成功"
        return data
