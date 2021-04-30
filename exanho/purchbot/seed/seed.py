from sqlalchemy.orm.session import Session as OrmSession
from exanho.orm.domain import Domain

from .settings import add_info
from .products import que_par_act
from .products import que_par_his
from .products import sub_par
from .products import rep_par_act
from .products import rep_par_his
from .products import rep_pars_con
from .vk import content as vk_content

def run():

    d = Domain('postgresql+psycopg2://kks:Nata1311@localhost/purchbot_test')
    with d.session_scope() as session:

        add_info.seed(session)

        que_par_act.seed(session)
        que_par_his.seed(session)
        # sub_par.seed(session)
        rep_par_act.seed(session)
        rep_par_his.seed(session)
        # rep_pars_con.seed(session)

        vk_content.seed(session)