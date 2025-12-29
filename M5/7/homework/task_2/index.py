from http_fw.router import Router
from http_fw.server import run

from app.tasks import TaskController

config = {
    'host': 'localhost',
    'port': 8000,
    'static': 'static'
}

router = Router()

router.get('/', TaskController, 'index')
router.get('/tasks', TaskController, 'index')
router.get('/tasks/new', TaskController, 'new')
router.get('/task',TaskController, 'view_task')
router.post('/tasks', TaskController, 'create')

run(router, config)
