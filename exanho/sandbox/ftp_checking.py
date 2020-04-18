import datetime
from exanho.eis44.ftp_consider import FtpConsider
import exanho.eis44.config as config

class MokiQueue:
    def put(self, tuple):
        print(tuple)

def run():
    insp_q = MokiQueue()
    viewer = FtpConsider(
                        task_id=1,
                        insp_q=insp_q,
                        host=config.ftp_host,
                        port=config.ftp_port,
                        user=config.ftp_user,
                        password=config.ftp_password,
                        location='/fcs_regions/Adygeja_Resp/*/currMonth',
                        min_date=datetime.datetime(2020, 4, 16, 0, 0, 1, 0), # 2020-04-16 00:00:01
                        # max_date=load_task.max_date,
                        excluded_folders= None,
                        delimiter='|'
                        )
    viewer.prepare()
    viewer.inspect()