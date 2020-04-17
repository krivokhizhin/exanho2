import datetime
from exanho.eis44.ftp_consider import FtpConsider
import exanho.eis44.config as config

def run():
    viewer = FtpConsider(
                        host=config.ftp_host,
                        port=config.ftp_port,
                        user=config.ftp_user,
                        password=config.ftp_password,
                        location='/fcs_fas/checkPlan/*',
                        min_date=datetime.datetime(2020, 1, 1, 0, 0, 0, 1),
                        # max_date=load_task.max_date,
                        excluded_folders= 'currMonth | prevMonth',
                        delimiter='|'
                        )
    viewer.prepare()
    viewer.inspect()