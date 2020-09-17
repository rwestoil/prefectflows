import sys
import prefect
from prefect import task, Flow, Parameter
from prefect.schedules import CronSchedule


sys.path.append('../pyoilfundy')

from pyoilfundy import fundyproducts as p

daily_7_sched = CronSchedule('0 7 * * 1-5')


def register_products_dash_flow():
    with Flow('product_by_region', schedule=daily_7_sched) as f:
        commods = ['lpg', 'naphtha', 'gasoline', 'diesel', 'jet', 'fueloil']
        p.make_specified_product_dash.map(commods)

    f.register(project_name='pyoilfundy')