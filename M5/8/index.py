from http_fw.router import Router
from http_fw.server import run
from app.expenses import ExpensesController
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

config = {
    'host': 'localhost',
    'port': 8000,
    'static':os.path.join(BASE_DIR, 'static') 
}


router = Router()

router.get('/',ExpensesController,'index')
router.get('/expenses',ExpensesController,'index')
router.get('/expenses/new',ExpensesController,'new')
router.post('/expenses', ExpensesController, 'create')
router.get('/stats',ExpensesController,'stats')
run(router,config)